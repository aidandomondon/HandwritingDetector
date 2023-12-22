from model import master_model

class MasterController():
    '''
    Instantiates the model and view and handles interactions between them.
    '''
    

    def __init__(self, labels :list[int]):
        self._model = master_model.MasterModel(labels)


    def get_current_prompt(self):
        '''
        Gets the current label the model is expecting the user to input.
        
        Defers to the `model`'s `current_prompt` property.
        '''
        return self._model.current_prompt
    

    def stroke(self, x, y):
        '''
        Adds a stroke to the model's internal array representing the user input space.
        
        Defers to the model's `stroke` method
        '''
        self._model.stroke(x, y)


    def accept_drawing(self):
        '''
        Adds the current grid contents to the database as a training image,
        clears the grid, and advances to the next prompt.
        '''
        self._model.make_training_image()
        self._model.clear_grid()
        self._model.next_prompt()