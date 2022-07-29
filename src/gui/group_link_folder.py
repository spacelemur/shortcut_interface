import tkinter as tk
from tkinter import ttk
from src.open_shortcut import open_shortcut

class GroupLinkFolder:
  def __init__(self, parent, link_group) -> None:
    self.frame = tk.LabelFrame(parent, text=link_group.name)

    # Set up gui interface
    if link_group.gui_type == 'button':
      # print(link_group.links.items())
      for link_name, link_path in link_group.links.items():
        # print(link_path)
        b = tk.Button(self.frame, text= link_name, command=lambda p=link_path : open_shortcut(p))
        b.pack(side = 'left')

    elif link_group.gui_type == 'combobox':
      print(link_group.links.keys())
      cb = ttk.Combobox(self.frame, values=list(link_group.links.keys()))
      cb.pack()
      b = tk.Button(self.frame, text='Go', command=lambda c_box=cb : open_shortcut(link_group.links[c_box.get()])) 
      b.pack(side = 'left')

    else:
      raise f"At the moment gui type {link_group.gui} is not implemented"

  def return_frame(self):
    return self.frame