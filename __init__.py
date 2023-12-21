from config import Config
import os
import sys

# Initialize configurations (stored in config.py's Config class)
Config.PROJECT_ROOT_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
Config.DB_PATH = os.path.join(Config.PROJECT_ROOT_DIR, 'store', 'user_store.db')
Config.NEW_IMAGES_CACHE_DIR = os.path.join(Config.PROJECT_ROOT_DIR, 'store', 'new_images_cache')
Config.MODEL_SAVE_PATH = os.path.join(Config.PROJECT_ROOT_DIR, 'store', 'saved_model', 'model.pt')
Config.EPOCHS = 3
Config.IMAGE_ENCODING_METHOD = 'utf-8'
Config.IMAGE_SIDE_LENGTH = 28
Config.GRID_STROKE_FULL_COLOR = 255
Config.GRID_STROKE_SEMI_COLOR = 128

# Add root directory to sys.path so all files lower in hierarchy can find config.py
# as well as each other
sys.path.append(Config.PROJECT_ROOT_DIR)

# # Testing initialize_db
# from model import initialize_db
# initialize_db.__main__()

# # Testing add_training_image
# from controller import add_training_image as add_training_image
# a = [[9, 2], [5, 3]]
# add_training_image.__main__(a, 1)

# # Testing fetch_new_images
# from model import fetch_new_images
# dl = fetch_new_images.__main__()

from controller import main_controller
from view import tk_view

ctrlr = main_controller.Controller()
# b = tk_view.TkViewBuilder()
# b.bind_to_controller(ctrlr).add_main_window().add_main_frame().add_tab_view().add_training_tab().add_testing_tab()
# tkv = b.build()
tkv = tk_view.TkView(ctrlr)
tkv.run()
