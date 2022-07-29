import tkinter as tk
from tkinter import ttk

class MainWindow:
  def __init__(self, parent, window_name='Shortcuts'):
    self.root = tk.Tk()
    self.frames = {}
    self.active = False
    self.sci_obj = parent

    self.root.title(window_name)

  def display_gui(self):
    self.root.mainloop()



  def close_gui(self):
    self.root.destroy()