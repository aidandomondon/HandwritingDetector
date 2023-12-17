###############################################################################
# Initializes the database to store user data
###############################################################################
import json
import sqlite3 as sql
from config import Config

# Creates the database
def _create_database():
    # '''connect''' function implicitly creates the database if 
    # it doesn't exist already
    sql.connect(Config.DB_PATH)


# Adds a table to store the training images created by the user
def _add_TrainingImage_table():
    with sql.connect(Config.DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(f'''
            CREATE TABLE TrainingImage (
                imageID INTEGER PRIMARY KEY NOT NULL,
                imageData BLOB,
                labelID INTEGER NOT NULL,
                timeAdded DATETIME NOT NULL,
                FOREIGN KEY (labelID) REFERENCES Label (labelID)
            );
        ''')


# Adds a table to store the generated adversarial examples
def _add_AdversarialImage_table():
    with sql.connect(Config.DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(f'''
            CREATE TABLE AdversarialImage (
                imageID INTEGER PRIMARY KEY NOT NULL,
                trueLabel INTEGER,
                trickLabel INTEGER,
                FOREIGN KEY (trueLabel) REFERENCES Label (labelID),
                FOREIGN KEY (trickLabel) REFERENCES Label (labelID)
            );
        ''')


# Adds and populates the table storing the possible labels
# (assumes we are predicting digits, [0, 9])
def _add_Label_table():
    with sql.connect(Config.DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(f'''
            CREATE TABLE Label (
                labelID INT NOT NULL PRIMARY KEY,
                label INT NOT NULL CHECK(label >= 0) CHECK(label <= 9)
            );
        ''')
        cursor.execute('INSERT INTO Label (labelID, label) VALUES (0, 0);')
        cursor.execute('INSERT INTO Label (labelID, label) VALUES (1, 1);')
        cursor.execute('INSERT INTO Label (labelID, label) VALUES (2, 2);')
        cursor.execute('INSERT INTO Label (labelID, label) VALUES (3, 3);')
        cursor.execute('INSERT INTO Label (labelID, label) VALUES (4, 4);')
        cursor.execute('INSERT INTO Label (labelID, label) VALUES (5, 5);')
        cursor.execute('INSERT INTO Label (labelID, label) VALUES (6, 6);')
        cursor.execute('INSERT INTO Label (labelID, label) VALUES (7, 7);')
        cursor.execute('INSERT INTO Label (labelID, label) VALUES (8, 8);')
        cursor.execute('INSERT INTO Label (labelID, label) VALUES (9, 9);')


def __main__():
    _create_database()
    _add_TrainingImage_table()
    _add_AdversarialImage_table()
    _add_Label_table()