###############################################################################
# Adds the given image to the user store as a training image
###############################################################################
import sqlite3 as sql
from config import Config

# Inserts the training image into the TrainingImage table
def _send_to_db(image_as_BLOB, label):
    with sql.connect(Config.DB_PATH) as connection:
        cursor = connection.cursor()
        # Find labelID for our label.
        # possible inefficiency here. since we have to query the db for the labelID
        # that corresponds to our label everytime we upload an image to it,
        # we're adding an extra query for each image upload.
        label_id = cursor.execute(
            f'''
                SELECT labelID FROM Label 
                    WHERE label = :label;
            ''',
            {"label": label}
        ).fetchone()[0]
        cursor.execute(
            f'''
                INSERT INTO TrainingImage (imageData, labelID, timeAdded)
                    VALUES (:imageData, :labelID, DATETIME('now'));
            ''',
            {"imageData": image_as_BLOB, "labelID": label_id}
        )


# Converts the given image to a SQLite BLOB by making a string of
# the represntation of the image as a 2D array and encoding it
def _image_to_BLOB(image :[[int]]):
    return sql.Binary(bytes(str(image), Config.IMAGE_ENCODING_METHOD))


def __main__(image :[[int]], label):
    _send_to_db(_image_to_BLOB(image), label)