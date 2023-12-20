import tkinter as tk 
from tkinter import ttk
from view import training_tab
from view import testing_tab

def __main__():
   # Main Window
   main_window = tk.Tk()
   main_window.title('Handwriting Detector')
   main_window.minsize(220, 165)

   # Main Frame
   main_frame = ttk.Frame(main_window, padding="3 3 12 12")
   main_frame.pack(expand=True, fill='both')

   # Tab View
   tab_view = ttk.Notebook(main_frame)
   tab_view.pack(expand=True, fill='both')

   # Create the training tab, register it under the tab view
   training_tab.training_tab(tab_view)

   # Create the testing tab, register it under the tab view
   testing_tab.testing_tab(tab_view)

   main_window.mainloop()