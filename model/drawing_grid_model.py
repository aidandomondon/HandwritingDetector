class DrawingGridModel():
    '''
    Two-dimensional array to internally represent the canvas state.
    '''


    def __init__(self, size):
        '''
        @param `size`   side length of the (square) canvas to be represented by
                        this model
        '''
        self.size = size
        self.arr = [[0 for j in range(size)] for i in range(size)]
        

    def write(self, i, j, value):
        '''
        Writes `value` into the cell at the `i`th row and `j`th column of
        this model's array if (i, j) is within the bounds of the array. If not,
        does nothing.

        @param `i` the row of the cell being written to
        @param `j` the column of the cell being written to
        @param `value` the value to write to the cell
        '''
        if j >= 0 and j < self.size and i >= 0 and i < self.size:
            self.arr[i][j] = value