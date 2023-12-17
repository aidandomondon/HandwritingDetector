###############################################################################
# Adds the given image to the user store as a training image
###############################################################################
import sqlite3 as sql
from config import Config


# Inserts the training image into the TrainingImage table
def _send_to_db(image_as_blob, label):
    with sql.connect(Config.DB_PATH) as connection:
        cursor = connection.cursor()
        # Find labelID for our label.
        # possible inefficiency here. since we have to query the db for the labelID
        # that corresponds to our label everytime we upload an image to it,
        # we're adding an extra query for each image upload.
        label_id = cursor.execute(f'''
            SELECT labelID FROM Label 
                WHERE label = {label};
        ''')
        cursor.execute(f'''
            INSERT INTO TrainingImage (imageData, labelID, timeAdded)
                VALUES ({image_as_blob}, {label_id}, DATE('now'));
        ''')


# Converts the given image to a SQLite BLOB
def _image_to_blob(image):
    pass


def __main__(image, label):
    _send_to_db(_image_to_blob, label)