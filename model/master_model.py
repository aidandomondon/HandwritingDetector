from os import path
from config import Config
from model import initialize_db
from model import drawing_grid_model
from model import prompter
from model import add_training_image

class MasterModel():
    '''
    Initializes all entities and orchestrates all services that the model promises.
    '''

    def __init__(self, labels):
        self._prompter = prompter.Prompter(labels)
        self.current_prompt = self._prompter.next()
        if not path.isfile(Config.DB_PATH):
            initialize_db.__main__()
        self._grid_model = drawing_grid_model.DrawingGridModel(Config.IMAGE_SIDE_LENGTH)


    def stroke(self, x, y):
        '''
        Updates the internal representation grid to reflect an added stroke.
        '''
        r = 1
        self._grid_model.write(y, x, Config.GRID_STROKE_FULL_COLOR)  # Center
        self._grid_model.write(y, x - r, Config.GRID_STROKE_SEMI_COLOR) # Left
        self._grid_model.write(y, x + r, Config.GRID_STROKE_SEMI_COLOR) # Right
        self._grid_model.write(y - r, x, Config.GRID_STROKE_SEMI_COLOR) # Bottom
        self._grid_model.write(y + r, x, Config.GRID_STROKE_SEMI_COLOR) # Top


    def clear_grid(self):
        '''
        Clears the model's internal representation of the user's input.
        '''
        self._grid_model.clear()

    
    def next_prompt(self):
        '''
        Gets the next label the user is to be prompted to procure an example for.
        '''
        self.current_prompt = self._prompter.next()

    
    def make_training_image(self):
        '''
        Adds the current grid contents / internal representation of the user's
        inputted image to the database.
        '''
        add_training_image.__main__(self._grid_model.arr, self.current_prompt)