from config import Config
import os
import sys

# Initialize configurations (stored in config.py's Config class)
Config.PROJECT_ROOT_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
Config.DB_PATH = os.path.join(Config.PROJECT_ROOT_DIR, 'store', 'user_store.db')
Config.NEW_IMAGES_CACHE_DIR = os.path.join(Config.PROJECT_ROOT_DIR, 'store', 'new_images_cache')
Config.MODEL_SAVE_PATH = os.path.join(Config.PROJECT_ROOT_DIR, 'store', 'saved_model', 'model.pt')
Config.EPOCHS = 3

# Add root directory to sys.path so all files lower in hierarchy can find config.py
sys.path.append(Config.PROJECT_ROOT_DIR)

from model import initialize_db as initialize_db
initialize_db.__main__()