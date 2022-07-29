import os
import yaml
from src.linkgroup import LinkGroup
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
      print(link_group.type) if self.debug else false
      if link_group.type == 'link':
        print('adding a link GroupLink') if self.debug else False
        group_frame = gui.GroupLink(self.gui.root, link_group)
      elif link_group.type == 'link_folder':
        print('adding a link GroupLinkFolder') if self.debug else False
        group_frame = gui.GroupLinkFolder(self.gui.root, link_group)
      elif link_group.type == 'link_list':
        print('adding a link GroupLinkList') if self.debug else False
        group_frame = gui.GroupLinkList(self.gui.root, link_group)
      else:
        raise f"Gui Link group error. Gui type is {link_group.gui_type}"
      f = group_frame.return_frame()
      f.pack()
      
    self.gui.display_gui()
      

  # def create_gui2(self):
  #   self.gui = MainWindow(self, self.shortcut_config)
  #   for sc_name, sc_def in self.shortcut_config.items():
  #     print(sc_name) if self.debug else False
  #     if sc_def['type'] == 'file':
  #       if 'Files' not in self.gui.frames:
  #         self.gui.create_frame('Files')
  #       #TODO: create a better method for accessing frames- gui method to return frame?
  #       self.gui.define_sc_button(self.gui.frames['Files'], sc_def['name'], sc_def['path'])
  #     elif sc_def['type'] == 'dir':
  #       group_name = sc_def['name']
  #       if group_name not in self.gui.frames:
  #         self.gui.create_frame(group_name)
  #         dirpath = sc_def['path']
  #         files = os.listdir(dirpath)
  #         #FIXME: displays entire file path in combo box. going to have to associate name with filepath and look up
  #         file_paths = [os.path.abspath(os.path.join(dirpath,file)) for file in files]
          # self.gui.define_sc_select_widget(self.gui.frames[group_name], file_paths)
        
      

    # self.gui.display_gui2()

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

if __name__=='__main__':
  sci = ShortcutInterface()
  sci.load_config()
  sci.parse_config()
  sci.create_gui()
  sci.finish()
