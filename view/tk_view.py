import tkinter as tk 
from tkinter import ttk
from view.training_tab import TrainingTabBuilder
from view import testing_tab
from controller import main_controller


class TkView():
   def run(self):
      if self.controller:  # "only if this view is bound to a controller"
         self.main_window.mainloop()


class TkViewBuilder():

   def bind_to_controller(self, controller :main_controller.Controller):
      self.controller = controller
      return self

   def add_main_window(self):
      self.main_window = tk.Tk()
      self.main_window.title('Handwriting Detector')
      self.main_window.minsize(220, 165)
      return self

   def add_main_frame(self):
      self.main_frame = ttk.Frame(self.main_window, padding="3 3 12 12")
      self.main_frame.pack(expand=True, fill='both')
      return self

   def add_tab_view(self):
      self.tab_view = ttk.Notebook(self.main_frame)
      self.tab_view.pack(expand=True, fill='both')
      return self

   def add_training_tab(self):
      ttb = TrainingTabBuilder().tabUnder(self.tab_view).bind_to_controller(self.controller).add_main_frame().add_prompt().add_drawing_pad()
      tt = ttb.build()
      self.training_tab = tt
      return self

   def add_testing_tab(self):
      self.testing_tab = testing_tab.testing_tab(self.tab_view)
      return self

   def build(self):
      v = TkView()
      v.controller = self.controller
      v.main_window = self.main_window
      v.main_frame = self.main_frame
      v.tab_view = self.tab_view
      v.testing_tab = self.testing_tab
      v.training_tab = self.training_tab
      return v