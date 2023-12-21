import tkinter as tk
import tkinter.ttk as ttk
from config import Config
from controller import main_controller

class TrainingTab():
    '''
    Includes the grid to draw the next training image, and the prompt for
    which digit the user should draw.
    '''

    def __init__(self, master_tab_view :ttk.Notebook, controller :main_controller.Controller):

        self.controller = controller

        self.master = master_tab_view

        self.frame = ttk.Frame(self.master)
        self.frame.pack(expand=True, fill='both')
        self.master.add(self.frame, text='Train')

        self.prompt = ttk.Label(self.frame, 
                                text=TrainingTab._prompt(self.controller.current_prompt))
        self.prompt.pack(expand=True, fill='both')

        self.canvas = tk.Canvas(self.frame, 
                                width=Config.IMAGE_SIDE_LENGTH, 
                                height=Config.IMAGE_SIDE_LENGTH)
        self.canvas.pack(expand=True)

        def on_mousedown(event):
            self._stroke(event.x, event.y)
            self.controller.stroke(event.x, event.y)
        self.canvas.bind("<B1-Motion>", on_mousedown)
        self.canvas.bind("<Button-1>", on_mousedown)

        def on_mouseup(event):
            self.controller.accept_drawing()
            self.prompt.config(text=self._prompt(self.controller.current_prompt))
            self.canvas.delete('all')
        self.canvas.bind("<ButtonRelease-1>", on_mouseup)


    # To keep track of / store the prompt displayed to users.
    # And to retrieve it.
    @staticmethod
    def _prompt(label :str) -> str:
        return f"Draw a {label}."
    

    # Fills the 4-neighborhood of the given point on the given canvas.
    # Fills the point's neighbors with a lighter color than used for point.
    def _stroke(self, x, y):
        
        full_color = "#000000"
        light_color = "#808080"
        r = 1
        self.canvas.create_rectangle(x, y, x, y, fill=full_color) # Center
        self.canvas.create_rectangle(x - r, y, x - r, y, fill=light_color) # Left
        self.canvas.create_rectangle(x + r, y, x + r, y, fill=light_color) # Right
        self.canvas.create_rectangle(x, y - r, x, y - r, fill=light_color) # Bottom
        self.canvas.create_rectangle(x, y + r, x, y + r, fill=light_color) # Top