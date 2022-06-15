import os
import tkinter as tk
import yaml

# Find file path and setup configuration
shortcut_dir_path = os.path.dirname(os.path.realpath(__file__)) #FIXME: Delete if not needed

class ShortcutInterface:
  def __init__(self, use_gui = True):
    self.debug = None
    self.use_gui = use_gui
    self.gui = None
    self.shortcut_config = None
    self.shortcuts_path = None

  def load_config(self, config_path = 'config.yml'):
    # Load tool configuration
    with open(config_path, 'r') as config_file:
      self.config = yaml.safe_load(config_file)

    # Define debug state
    self.debug = self.config['debug']
    print("Debugging on") if self.debug else False

    # Load shortcuts
    self.shortcuts_path = self.config['shortcuts']['path']
    with open(self.shortcuts_path, 'r') as shortcut_config_file:
      self.shortcut_config = yaml.safe_load(shortcut_config_file)
      print(f"\n{self.shortcut_config}") if self.debug else False

  def create_gui(self):
    self.gui = ShortcutGui(self, self.shortcut_config)
    self.gui.display_gui()

  def finish(self):
    if self.gui.active:
      # Captures case if window has already be closed.... not the best
      try:
        self.gui.close_gui()
      except:
        pass
    exit

  def open_shortcut(self, shortcut_path):
    os.startfile(shortcut_path)
    print(self.use_gui)
    if self.use_gui:
      print('true condition satisfied') if self.debug  else False
      self.finish()


class ShortcutGui:
  def __init__(self, sci_obj, sci_array):
    self.root = tk.Tk()
    self.sci_array = sci_array
    self.active = False
    self.sci_obj = sci_obj

  def display_gui(self):
    interfaces = self.sci_array.keys()
    for i in interfaces:
      frame = tk.Frame(self.root)
      item = self.sci_array[i]
      if item['type'] == 'file':
        print(f'adding button for {item["name"]}') if self.sci_obj.debug else False
        new_button = self.define_button(frame, item['name'], item['path']) #TODO: fix this to based on absolute/relative
        new_button.pack()
      frame.pack()
    self.active = True
    self.root.mainloop()

  def define_button(self, parent, buttonlabel, path):
    b = tk.Button(parent, text= buttonlabel, command=lambda p=path : self.sci_obj.open_shortcut(p))
    return b


  def close_gui(self):
    self.root.destroy()




if __name__=='__main__':
  sci = ShortcutInterface()
  sci.load_config()
  sci.create_gui()
  sci.finish()
