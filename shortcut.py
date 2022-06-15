import os
import tkinter as tk
import yaml

# Find file path and setup configuration
shortcut_dir_path = os.path.dirname(os.path.realpath(__file__))

class ShortcutInterface:
  def __init__(self, use_gui = True):
    self.use_gui = use_gui
    self.gui = None
    self.shortcut_config = None
    self.shortcuts_path = None
    

  def load_config(self, config_path = 'config.yml'):
    # Load tool configuration
    with open(config_path, 'r') as config_file:
      self.config = yaml.safe_load(config_file)

    # Load shortcuts
    self.shortcuts_path = self.config['shortcuts']['path']
    with open(self.shortcuts_path, 'r') as shortcut_config_file:
      self.shortcut_config = yaml.safe_load(shortcut_config_file)
      print(f"\n{self.shortcut_config}")

  def create_gui(self):
    self.gui = ShortcutGui(self.shortcut_config)
    self.gui.display_window()

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
        print(f'adding button for {item["name"]}')
        new_button = self.define_button(frame, item['name'], item['path']) #TODO: fix this to based on absolute/relative
        new_button.pack()
      frame.pack()
    self.root.mainloop()

  def define_button(self, parent, buttonlabel, path):
    b = tk.Button(parent, text= buttonlabel, command=lambda p=path : os.startfile(p))
    return b




if __name__=='__main__':
  sci = ShortcutInterface()
  sci.load_config()
  sci.create_gui()
