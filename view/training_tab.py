import tkinter as tk
import tkinter.ttk as ttk
from controller import add_training_image

FIXED_SIZE = 28

# Fills the 4-neighborhood of the given point on the given canvas.
# Fills the point's neighbors with a lighter color than used for point.
# Updates the internal representation of the grid to reflect the added stroke.
def _stroke(canvas, internal_model, x, y):
    full_color = "#000000"
    light_color = "#808080"
    full_color_internal = 255   # pixel intensity to be given to the center
    light_color_internal = 128  # pixel intensity to be given to the neighbors
    r = 1

    def check_range(x, y):
        return x >= 0 and x < FIXED_SIZE and y >= 0 and y < FIXED_SIZE

    # Center
    if check_range(x, y):
        canvas.create_rectangle(x, y, x, y, fill=full_color)
        internal_model[y][x] = full_color_internal

    # Left neighbor
    if check_range(x - r, y):
        canvas.create_rectangle(x - r, y, x - r, y, fill=light_color)
        internal_model[y][x - r] = light_color_internal

    # Right neighbor
    if check_range(x + r, y):
        canvas.create_rectangle(x + r, y, x + r, y, fill=light_color)
        internal_model[y][x + r] = light_color_internal

    # Bottom neighbor
    if check_range(x, y - r):
        canvas.create_rectangle(x, y - r, x, y - r, fill=light_color)
        internal_model[y - r][x] = light_color_internal

    # Top neighbor
    if check_range(x, y + r):
        canvas.create_rectangle(x, y + r, x, y + r, fill=light_color)
        internal_model[y + r][x] = light_color_internal


def training_tab(tab_view :ttk.Notebook):
    '''
    Returns a `tkinter.Frame` containing the contents of the training tab.
    Includes the grid to draw the next training image, and the prompt for
    which digit the user should draw.

    @tab_view: The `ttk.Notebook` tab view to which this tab will be added.
    '''

    # root frame
    training_tab = ttk.Frame(tab_view)
    training_tab.pack(expand=True, fill='both')
    tab_view.add(training_tab, text='Train')

    # prompt users on what number to draw
    training_tab_prompt = ttk.Label(training_tab, text=f"Draw a {7}.")
    training_tab_prompt.pack(expand=True, fill='both')

    # drawing pad
    # initialize 2d array as internal representation of the canvas state
    model = [[0 for j in range(FIXED_SIZE)] for i in range(FIXED_SIZE)]
    drawing_pad = tk.Canvas(training_tab, width=FIXED_SIZE, height=FIXED_SIZE)
    drawing_pad.pack(expand=True)
    # function left unnamed to convey that it is simply a wrapper 
    def _f(event): 
        _stroke(drawing_pad, model, event.x, event.y)
    drawing_pad.bind("<B1-Motion>", _f)
    drawing_pad.bind("<Button-1>", _f)

    # drawing_pad.bind("<ButtonRelease-1>", add_training_image.__main__())
    return training_tab