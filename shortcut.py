import os
import tkinter as tk
import yaml

# Find file path and setup configuration
shortcut_dir_path = os.path.dirname(os.path.realpath(__file__))

class ShortcutInterface:
  def __init__(self):
    self.config = None
    

  def load_config(self, config_path = 'config.yml'):
    with open(config_path, 'r') as config_file:
      self.config = yaml.safe_load(config_file)
      print(f"\n{self.config}")
      print(self.config['dirs']['type'])


class ShortcutGui:
  def __init__(self, sci_array):
    self.root = tk.Tk()
    self.sci_array = sci_array

  def display_window(self):
    interfaces = self.sci_array.keys()
    for i in interfaces:
      frame = tk.Frame(self.root)
      item = self.sci_array[i]
      if item['type'] == 'file':
        new_button = self.define_button(frame, item['name'], item['path']) #TODO: fix this to based on absolute/relative
        frame.append(new_button)
        new_button.pack()
      frame.pack()
    self.root.mainloop()

  def define_button(self, parent, buttonlabel, path):
    b = tk.Button(parent, text= buttonlabel, command=lambda p=path : os.os.startfile(p))
    return b




if __name__=='__main__':
  sci = ShortcutInterface()
  sci.load_config()
  gui = ShortcutGui(sci.config)
  gui.display_window()
