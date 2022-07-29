import tkinter as tk
from src.open_shortcut import open_shortcut

class GroupLink:
  def __init__(self, parent, linkgroup) -> None:
    self.frame = tk.LabelFrame(parent, text=linkgroup.name)

    # Set up gui interface
    if linkgroup.gui_type == 'button':
      print(linkgroup.links)
      link_name = list(linkgroup.links.keys())[0]
      path = list(linkgroup.links.values())[0]
      b = tk.Button(self.frame, text= link_name, command=lambda p=path : open_shortcut(p))
      b.pack()
    else:
      raise "At the moment GroupLink gui elements only work with button gui types"

  def return_frame(self):
    return self.frame