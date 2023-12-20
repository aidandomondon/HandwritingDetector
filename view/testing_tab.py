import tkinter as tk
from tkinter import ttk as ttk

def testing_tab(tab_view):
    '''
    Returns a `tkinter.Frame` containing the contents of the testing tab.

    @tab_view: The `ttk.Notebook` tab view to which this tab will be added.
    '''
    testing_tab = ttk.Frame(tab_view)
    testing_tab.pack(expand=True, fill='both')
    tab_view.add(testing_tab, text='Test')