from os import path
from config import Config
from model import initialize_db
from model import drawing_grid_model
from model import prompter
from model import add_training_image
from model import classify_image

class MasterModel():
    '''
    Initializes all entities and orchestrates all services that the model promises.
    '''

    def __init__(self, labels):
        self._prompter = prompter.Prompter(labels)
        self.current_prompt = self._prompter.next()
        if not path.isfile(Config.DB_PATH):
            initialize_db.__main__()
        self._training_grid = drawing_grid_model.DrawingGridModel(Config.IMAGE_SIDE_LENGTH)
        self._testing_grid = drawing_grid_model.DrawingGridModel(Config.IMAGE_SIDE_LENGTH)


    @staticmethod
    def _stroke_helper(grid :drawing_grid_model.DrawingGridModel, x, y):
        r = 1
        grid.write(y, x, Config.GRID_STROKE_FULL_COLOR)  # Center
        grid.write(y, x - r, Config.GRID_STROKE_SEMI_COLOR) # Left
        grid.write(y, x + r, Config.GRID_STROKE_SEMI_COLOR) # Right
        grid.write(y - r, x, Config.GRID_STROKE_SEMI_COLOR) # Bottom
        grid.write(y + r, x, Config.GRID_STROKE_SEMI_COLOR) # Top

    def stroke_train(self, x, y):
        '''
        Updates the internal representation of user training input to reflect an added stroke.
        '''
        MasterModel._stroke_helper(self._training_grid, x, y)

    def stroke_test(self, x, y):
        '''
        Updates the internal representation of user test input to reflect an added stroke.
        '''
        self._stroke_helper(self._testing_grid, x, y)


    def clear_grid_train(self):
        '''
        Clears the model's internal representation of the user's input.
        '''
        self._training_grid.clear()
    
    def clear_grid_test(self):
        '''
        Clears the model's internal representation of the user's test input.
        '''
        self._testing_grid.clear()

    
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
        add_training_image.__main__(self._training_grid.arr, self.current_prompt)

    def classify_image(self) -> str:
        '''
        Classifies the current testing grid contents.
        '''
        return classify_image.__main__(self.training_grid.arr)