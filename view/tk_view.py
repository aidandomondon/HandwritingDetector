import tkinter as tk 
from tkinter import ttk
from controller import master_controller
from view.training_tab import TrainingTab
from view import testing_tab


class TkView():
   '''
   A Tk user interface for the app using `tkinter`.
   '''

   def __init__(self, controller :master_controller.MasterController):

      self.controller = controller

      self.main_window = tk.Tk()
      self.main_window.title('Handwriting Detector')
      self.main_window.minsize(220, 165)

      self.main_frame = ttk.Frame(self.main_window, padding="3 3 12 12")
      self.main_frame.pack(expand=True, fill='both')

      self.tab_view = ttk.Notebook(self.main_frame)
      self.tab_view.pack(expand=True, fill='both')

      self.training_tab = TrainingTab(self.tab_view, self.controller)

      self.testing_tab = testing_tab.testing_tab(self.tab_view)


   def run(self):
      '''
      To start the Tk interface.
      '''
      self.main_window.mainloop()