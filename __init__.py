from config import Config
import os
import sys

# Initialize configurations (stored in config.py's Config class)
Config.PROJECT_ROOT_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
Config.DB_PATH = os.path.join(Config.PROJECT_ROOT_DIR, 'store', 'user_store.db')
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




# Testing MVC
from controller import master_controller
from view import tk_view

labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ctrlr = master_controller.MasterController(labels)
tkv = tk_view.TkView(ctrlr)
tkv.run()




# # Testing train.py
# from model import fetch_new_images
# from model import initial_classifier
# from torch.nn import CrossEntropyLoss
# from model import train

# dl = fetch_new_images.__main__()
# arch = initial_classifier.InitialClassifier
# loss_fn = CrossEntropyLoss()
# train.__main__(dl, arch, loss_fn)




# # Testing classification
# from model import classify_image
# from random import randint
# from torch import Tensor
# test_image = [[randint(0, 255) for j in range(Config.IMAGE_SIDE_LENGTH)] for i in range(Config.IMAGE_SIDE_LENGTH)]
# test_image = [test_image]
# test_image = Tensor(test_image)
# print(test_image.shape)
# classify_image.__main__(test_image)