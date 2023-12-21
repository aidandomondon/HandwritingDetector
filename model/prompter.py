from random import shuffle
from random import random
from random import seed

class Prompter():
    '''
    To manage the labels the user is being prompted to draw.
    '''

    def __init__(self, possible_labels :set, seed :int = None):
        if possible_labels == []:
            raise Exception('Illegal argument: empty list')
        else:
            self._possible_labels = list(possible_labels) # sets are not mutable
            self._idx = -1
            if seed:
                seed(seed)
    

    def next(self):
        self._idx += 1
        if self._idx == len(self._possible_labels):
            shuffle(self._possible_labels)
            self._idx = 0
        return self._possible_labels[self._idx]