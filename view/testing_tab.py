from config import Config
import tkinter as tk
from tkinter import ttk as ttk
from controller import master_controller

class TestingTab():
    '''
    Containins the contents of the testing tab.
    '''

    def __init__(self, master_tab_view :ttk.Notebook, controller :master_controller.MasterController):
        
        self._controller = controller

        self._frame = ttk.Frame(master_tab_view)
        self._frame.pack(expand=True, fill='both')
        master_tab_view.add(self._frame, text='Test')

        self._prompt = ttk.Label(self._frame, text='That looks like a: ')
        self._prompt.pack(expand=True, fill='both')

        self._canvas = tk.Canvas(self._frame, 
                                width=Config.IMAGE_SIDE_LENGTH, 
                                height=Config.IMAGE_SIDE_LENGTH)
        self._canvas.pack(expand=True)

        def on_mousedown(event):
            self._stroke(event.x, event.y)
            self._controller.stroke_test(event.x, event.y)
        self._canvas.bind("<B1-Motion>", on_mousedown)
        self._canvas.bind("<Button-1>", on_mousedown)

        def on_mouseup(event):
            self._controller.classify_drawing() # submit current grid to db and clear grid for new storage
            self._canvas.delete('all')        # wipe visual representation of grid (drawing pad)
        self._canvas.bind("<ButtonRelease-1>", on_mouseup)


    # ABSTRACT THIS OUT FROM TestingTab and TrainingTab
    # Fills the point's neighbors with a lighter color than used for point.
    def _stroke(self, x, y):
        full_color = "#000000"
        light_color = "#808080"
        r = 1
        self._canvas.create_rectangle(x, y, x, y, fill=full_color) # Center
        self._canvas.create_rectangle(x - r, y, x - r, y, fill=light_color) # Left
        self._canvas.create_rectangle(x + r, y, x + r, y, fill=light_color) # Right
        self._canvas.create_rectangle(x, y - r, x, y - r, fill=light_color) # Bottom
        self._canvas.create_rectangle(x, y + r, x, y + r, fill=light_color) # Top