###############################################################################
# Retrieves images added since the given time and packages in a PyTorch Dataloader
###############################################################################
import sqlite3 as sql
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from config import Config
import ast
from torch import Tensor


# queries the database for the last time images were fetched
def _last_update():
    result = None
    with sql.connect(Config.DB_PATH) as connection:
        cursor = connection.cursor()
        result = cursor.execute(
            f'''
                SELECT timeFetched FROM FetchNewTrainingImagesInstance
                    ORDER BY timeFetched DESC
            '''
        ).fetchall()
    return 0 if result == [] else result[0][0]


# queries the database for all training images added after the specified time
def _query(since):
    results = None
    with sql.connect(Config.DB_PATH) as connection:
        cursor = connection.cursor()
        results = cursor.execute(
            f'''
                SELECT TrainingImage.imageData, Label.label 
                    FROM TrainingImage INNER JOIN Label
                        ON TrainingImage.labelID = Label.labelID
                    WHERE timeAdded > ?;
            ''',
            (since,)
        ).fetchall()
    return results


# torch.utils.data.Dataset implementation to store user images
class _TrainingImageDataset(Dataset):

    # Decodes the BLOB containing the image data for each result in the given 
    # array of query results
    @staticmethod
    def decode_BLOB(query_results):
        decoded_results = []
        for result in query_results:
            decoded_image = bytes.decode(result[0], Config.IMAGE_ENCODING_METHOD)
            decoded_image = ast.literal_eval(decoded_image)
            decoded_image = Tensor(decoded_image)
            decoded_results.append((decoded_image, result[1]))
        return decoded_results

    def __init__(self, query_results):
        self.samples = _TrainingImageDataset.decode_BLOB(query_results)
        
    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        return self.samples[idx]


# Loads query result of images into a PyTorch dataset, dataloader
# Mandates a batch size of 1. 
# *** may be possible to change to have a dynamic batch size equal 
# to however many new images were fetched each time. Future implementation?
def _to_dataloader(query_results):
    return DataLoader(_TrainingImageDataset(query_results), 1)


# Creates a new FetchNewTrainingImagesInstance entry
def _mark_as_fetched():
    with sql.connect(Config.DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            f'''
                INSERT INTO FetchNewTrainingImagesInstance (timeFetched) 
                    VALUES (DATETIME('now'));
            '''
        )


def __main__():
    '''
    Fetches new images added to the database since the last query.
    Packages them in a `torch.utils.data.DataLoader`
    '''
    new_images = _query(since=_last_update())
    dataloader = _to_dataloader(new_images)
    _mark_as_fetched()
    return dataloader