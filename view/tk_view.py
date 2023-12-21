import tkinter as tk 
from tkinter import ttk
from controller import main_controller
from view.training_tab import TrainingTab
from view import testing_tab


class TkView():
   '''
   A Tk user interface for the app using `tkinter`.
   '''

   def __init__(self, controller :main_controller.Controller):

      self.controller = controller

      self.main_window = tk.Tk()
      self.main_window.title('Handwriting Detector')
      self.main_window.minsize(220, 165)

      self.main_frame = ttk.Frame(self.main_window, padding="3 3 12 12")
      self.main_frame.pack(expand=True, fill='both')

      self.tab_view = ttk.Notebook(self.main_frame)
      self.tab_view.pack(expand=True, fill='both')

      # ttb = TrainingTabBuilder().tabUnder(self.tab_view).bind_to_controller(self.controller).add_main_frame().add_prompt().add_drawing_pad()
      # tt = ttb.build()
      self.training_tab = TrainingTab(self.tab_view, self.controller)

      self.testing_tab = testing_tab.testing_tab(self.tab_view)

   def run(self):
      self.main_window.mainloop()