import os
import tkinter as tk
from tkinter import ttk
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

  def create_gui2(self):
    self.gui = ShortcutGui(self, self.shortcut_config)
    for sc_name, sc_def in self.shortcut_config.items():
      print(sc_name) if self.debug else False
      if sc_def['type'] == 'file':
        if 'Files' not in self.gui.frames:
          self.gui.create_frame('Files')
        #TODO: create a better method for accessing frames- gui method to return frame?
        self.gui.define_sc_button(self.gui.frames['Files'], sc_def['name'], sc_def['path'])
      elif sc_def['type'] == 'dir':
        group_name = sc_def['name']
        if group_name not in self.gui.frames:
          self.gui.create_frame(group_name)
          dirpath = sc_def['path']
          files = os.listdir(dirpath)
          #FIXME: displays entire file path in combo box. going to have to associate name with filepath and look up
          file_paths = [os.path.abspath(os.path.join(dirpath,file)) for file in files]
          self.gui.define_sc_select_widget(self.gui.frames[group_name], file_paths)
        
      

    self.gui.display_gui2()

  def finish(self):
    if self.gui.active:
      # Captures case if window has already be closed.... not the best
      try:
        self.gui.close_gui()
      except:
        pass
    exit

  def open_shortcut(self, shortcut_path):
    os.startfile(shortcut_path) #TODO: fix this to based on absolute/relative path inputs
    print(self.use_gui)
    if self.use_gui:
      print('true condition satisfied') if self.debug  else False
      self.finish()


class ShortcutGui:
  def __init__(self, sci_obj, sci_array):
    self.root = tk.Tk()
    self.frames = {}

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
        new_button = self.define_sc_button(frame, item['name'], item['path']) 
        new_button.pack()
      frame.pack()
    self.active = True
    self.root.mainloop()

  def display_gui2(self):
    self.active = True
    self.root.mainloop()

  def create_frame(self, fname):
    f = tk.LabelFrame(self.root, text = fname)
    f.pack(side='left')
    self.frames[fname] = f


  def define_sc_button(self, parent, buttonlabel, path):
    b = tk.Button(parent, text= buttonlabel, command=lambda p=path : self.sci_obj.open_shortcut(p))
    b.pack()
    return b

  def define_sc_select_widget(self, parent, list):
    cb = ttk.Combobox(parent, values=list)
    cb.pack()
    b = tk.Button(parent, text='Go', command=lambda c_box=cb : self.get_and_go(c_box))
    b.pack()

  #todo: rename
  def get_and_go(self, combo_box):
    print('get and go running')
    selection = combo_box.get()
    print(f"selection: {selection}")
    self.sci_obj.open_shortcut(selection)


  def close_gui(self):
    self.root.destroy()


if __name__=='__main__':
  sci = ShortcutInterface()
  sci.load_config()
  sci.create_gui2()
  sci.finish()
