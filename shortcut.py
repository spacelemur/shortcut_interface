import os
import tkinter as tk
import yaml

# Find file path and setup configuration
shortcut_dir_path = os.path.dirname(os.path.realpath(__file__))
#print(shortcut_dir_path)


def load_config():
  with open('config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)
    print(f"\n{config}")
    print(config['dirs']['type'])

class ShortcutGui:
  def __init__(self):
    self.root = tk.Tk()


  def display_window(self):
    self.root.mainloop()