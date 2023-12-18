###############################################################################
# Retrieves images added since the given time and packages in a PyTorch Dataloader
###############################################################################
import sqlite3 as sql
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from config import Config


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
    return 0 if result == [] else result[0]


# queries the database for all training images added after the specified time
def _query(since):
    result = None
    with sql.connect(Config.DB_PATH) as connection:
        cursor = connection.cursor()
        result = cursor.execute(
            f'''
                SELECT TrainingImage.imageData, Label.label 
                    FROM TrainingImage INNER JOIN Label
                        ON TrainingImage.labelID = Label.labelID
                    WHERE timeAdded > ?;
            ''',
            (since,)
        ).fetchall()
    return result


# torch.utils.data.Dataset implementation to store user images
class TrainingImageDataset(Dataset):

    def __init__(self, result):
        self.result = result

    def __len__(self):
        return len(self.result)

    def __getitem__(self, idx):
        return self.result[idx]


# Loads query result of images into a PyTorch dataset, dataloader
# Mandates a batch size of 1. 
# *** may be possible to change to have a dynamic batch size equal 
# to however many new images were fetched each time. Future implementation?
def _to_dataloader(query_result):
    return DataLoader(TrainingImageDataset(query_result), 1)


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
    new_images = _query(since=_last_update())
    res = _to_dataloader(new_images)
    _mark_as_fetched()
    return res