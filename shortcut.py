import os
import yaml
from src.link_group import LinkGroup
from src import gui
import pprint

# Find file path and setup configuration
shortcut_dir_path = os.path.dirname(os.path.realpath(__file__)) #FIXME: Delete if not needed

class ShortcutInterface:
  def __init__(self, use_gui = True):
    self.use_gui = use_gui
    self.config = None
    self.debug = None
    self.shortcuts_path = None
    self.shortcut_config = None
    self.link_groups = []
    self.gui = None

  def load_config(self, config_path = 'config.yml'):
    # Load tool configuration
    with open(config_path, 'r') as config_file:
      self.config = yaml.safe_load(config_file)

    # Define debug state
    self.debug = self.config['debug']
    print("Debugging on") if self.debug else False

    # Load shortcuts
    self.shortcuts_path = self.config['shortcuts_config']['path']
    with open(self.shortcuts_path, 'r') as shortcut_config_file:
      self.shortcut_config = yaml.safe_load(shortcut_config_file)
    pprint.pprint(self.shortcut_config) if self.debug else False

  def parse_config(self):
    config = self.shortcut_config
    print("\n\nConfig:") if self.debug else False
    pprint.pprint(config.items()) if self.debug else False
    for parameters in config.values():
      self.link_groups += [LinkGroup(parameters)]

  def create_gui(self):
    print("\n\nCreate Gui:") if self.debug else False
    self.gui = gui.MainWindow(self, self.shortcut_config)
    for link_group in self.link_groups:
      print(link_group.type) if self.debug else False
      group_frame = gui.LinkGroupFrame(self.gui, link_group)
      f = group_frame.return_frame()
      f.pack(side='left', fill='both')
      
    self.gui.display_gui()

  def finish(self):
    if self.gui.active:
      # Captures case if window has already be closed.... not the best
      try:
        self.gui.close_gui()
      except:
        pass
    exit

  def open_shortcut(self, shortcut_path): #FIXME:Depreciated 
    os.startfile(shortcut_path) #TODO: fix this to based on absolute/relative path inputs
    print(self.use_gui)
    if self.use_gui:
      print('true condition satisfied') if self.debug  else False
      self.finish()

if __name__=='__main__':
  sci = ShortcutInterface()
  sci.load_config()
  sci.parse_config()
  sci.create_gui()
  sci.finish()
