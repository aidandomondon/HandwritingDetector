import tkinter as tk
import tkinter.ttk as ttk
from config import Config
from controller import main_controller

class TrainingTab():
    '''
    Includes the grid to draw the next training image, and the prompt for
    which digit the user should draw.
    '''

    def stroke(self, x, y):
        '''
        Fills the 4-neighborhood of the given point on the given canvas.
        Fills the point's neighbors with a lighter color than used for point.
        '''
        
        full_color = "#000000"
        light_color = "#808080"
        r = 1
        self.drawing_pad.create_rectangle(x, y, x, y, fill=full_color) # Center
        self.drawing_pad.create_rectangle(x - r, y, x - r, y, fill=light_color) # Left
        self.drawing_pad.create_rectangle(x + r, y, x + r, y, fill=light_color) # Right
        self.drawing_pad.create_rectangle(x, y - r, x, y - r, fill=light_color) # Bottom
        self.drawing_pad.create_rectangle(x, y + r, x, y + r, fill=light_color) # Top


class TrainingTabBuilder():
    '''
    Breaks construction of `TrainingTab` into smaller logical units.
    '''

    def tabUnder(self, master_tab_view :ttk.Notebook):
        self.master = master_tab_view
        return self

    def bind_to_controller(self, controller :main_controller.Controller):
        self.controller = controller
        return self
    
    def add_main_frame(self):
        self.frame = ttk.Frame(self.master)
        self.frame.pack(expand=True, fill='both')
        self.master.add(self.frame, text='Train')
        return self
    
    def add_prompt(self):
        self.prompt = ttk.Label(self.frame, text=f"Draw a {7}.")
        self.prompt.pack(expand=True, fill='both')
        return self

    def add_drawing_pad(self):
        self.drawing_pad = tk.Canvas(self.frame, 
                                width=Config.IMAGE_SIDE_LENGTH, 
                                height=Config.IMAGE_SIDE_LENGTH)
        self.drawing_pad.pack(expand=True)
        return self
        
    @staticmethod
    def bind_drawing_pad(controller, training_tab):
        def _f(event): # function left unnamed to convey its simply a wrapper
            training_tab.stroke(event.x, event.y)
            controller.stroke(event.x, event.y)
        training_tab.drawing_pad.bind("<B1-Motion>", _f)
        training_tab.drawing_pad.bind("<Button-1>", _f)
        training_tab.drawing_pad.bind("<ButtonRelease-1>",
                                      lambda e: controller.add_training_image())
        
    def build(self):
        tt = TrainingTab()
        tt.controller = self.controller
        tt.main_frame = self.frame
        tt.prompt = self.prompt
        tt.drawing_pad = self.drawing_pad
        TrainingTabBuilder.bind_drawing_pad(tt.controller, tt)
        return tt
