#FIXME: i think this is going to be the exact same as a link folder.... why not make them the same, more generic thing!?!


import tkinter as tk
from tkinter import ttk
from src.open_shortcut import open_shortcut

class GroupLinkList:
  def __init__(self, parent, linkgroup) -> None:
    self.frame = tk.LabelFrame(parent, text=linkgroup.name)

    # Set up gui interface
    if linkgroup.gui_type == 'button':
      for link_name, link_path in linkgroup.links.items():
        b = tk.Button(self.frame, text= link_name, command=lambda p=link_path : open_shortcut(p))
        b.pack()

    elif linkgroup.gui_type == 'combobox':
      cb = ttk.Combobox(parent, values=linkgroup.links.keys())
      cb.pack()
      b = tk.Button(parent, text='Go', command=lambda c_box=cb : open_shortcut(linkgroup.links[c_box])) #FIXME: this probably won't work
      b.pack()

    else:
      raise f"At the moment gui type {linkgroup.gui} is not implemented"

  def return_frame(self):
    return self.frame