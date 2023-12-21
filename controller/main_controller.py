from config import Config
from controller import add_training_image
from model import drawing_grid_model
from model import prompter

class Controller():
    '''
    Instantiates the model and view and handles interactions between them.
    '''
    
    def __init__(self):
        self.grid = drawing_grid_model.DrawingGridModel(
            Config.IMAGE_SIDE_LENGTH)
        self.prompter = prompter.Prompter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.current_prompt = self.prompter.next()


    def stroke(self, x, y):
        '''
        Updates the internal representation grid to reflect an added stroke.
        '''
        r = 1
        self.grid.write(y, x, Config.GRID_STROKE_FULL_COLOR)  # Center
        self.grid.write(y, x - r, Config.GRID_STROKE_SEMI_COLOR) # Left
        self.grid.write(y, x + r, Config.GRID_STROKE_SEMI_COLOR) # Right
        self.grid.write(y - r, x, Config.GRID_STROKE_SEMI_COLOR) # Bottom
        self.grid.write(y + r, x, Config.GRID_STROKE_SEMI_COLOR) # Top

    
    def add_training_image(self):
        add_training_image.__main__(self.grid.arr, self.current_prompt)