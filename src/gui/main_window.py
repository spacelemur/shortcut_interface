import tkinter as tk
from tkinter import ttk

class MainWindow:
  def __init__(self, parent, sci_array):
    self.root = tk.Tk()
    self.frames = {}
    self.sci_array = sci_array
    self.active = False
    self.sci_obj = parent

  def display_gui(self):
    self.root.mainloop()

  def create_frame(self, fname): #FIXME: Depreciated
    f = tk.LabelFrame(self.root, text = fname)
    f.pack(side='left') 
    self.frames[fname] = f


  def define_sc_button(self, parent, buttonlabel, path): #FIXME: Depreciated
    b = tk.Button(parent, text= buttonlabel, command=lambda p=path : self.sci_obj.open_shortcut(p))
    b.pack()
    return b

  def define_sc_select_widget(self, parent, list): #FIXME: Depreciated
    cb = ttk.Combobox(parent, values=list)
    cb.pack()
    b = tk.Button(parent, text='Go', command=lambda c_box=cb : self.follow_link(c_box))
    b.pack()

  #todo: rename
  def follow_link(self, combo_box): #FIXME: Depreciated
    print('get and go running')
    selection = combo_box.get()
    print(f"selection: {selection}")
    self.sci_obj.open_shortcut(selection)


  def close_gui(self):
    self.root.destroy()