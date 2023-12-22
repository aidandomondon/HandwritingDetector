from model import master_model
from model import train_on_new_images

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
    

    def stroke_train(self, x, y):
        '''
        Adds a stroke to the model's internal array representing the 
        input space for the user's training images.
        
        Defers to the model's `stroke` method
        '''
        self._model.stroke_train(x, y)


    def stroke_test(self, x, y):
        '''
        Adds a stroke to the model's internal array representing the 
        input space for the user's test images.
        
        Defers to the model's `stroke_test` method
        '''
        self._model.stroke_test(x, y)


    def accept_drawing(self):
        '''
        Adds the current grid contents to the database as a training image,
        clears the grid, and advances to the next prompt. Starts training
        of the neural net on this example and any others that might not have
        been fetched.
        '''
        self._model.make_training_image()
        train_on_new_images.__main__()
        self._model.clear_grid_train()
        self._model.next_prompt()


    def get_prediction(self):
        result = self._model.classify_image()
        self._model.clear_grid_test()
        return result