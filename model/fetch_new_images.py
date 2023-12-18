###############################################################################
# Retrieves images added since the given time and packages in a PyTorch Dataloader
###############################################################################
import sqlite3 as sql
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from config import Config


# queries the database for all training images added after the specified time
def _query(since):
    result = None
    with sql.connect(Config.DB_PATH) as connection:
        cursor = connection.cursor()
        result = cursor.execute(
            f'''
                SELECT * FROM TrainingImage
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
def _to_dataloader(query_result):
    return DataLoader(TrainingImageDataset(query_result), 1)


# Creates a new FetchNewTrainingImagesInstance entry
def _mark_as_fetched():
    with sql.connect(Config.DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            f'''
                INSERT INTO FetchNewTrainingImagesInstance (timeFetched) 
                    VALUES (Date('now'));
            '''
        )


def __main__(since):
    _to_dataloader(_query(since))
    _mark_as_fetched()


