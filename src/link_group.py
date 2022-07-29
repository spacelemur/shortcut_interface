import os 
import yaml
class LinkGroup:
  def __init__(self, dict):
    print('Creating a LinkGroup!')
    self.dict = dict
    self.name = dict['group_name']
    self.type = dict['type']
    self.path_type = dict['path_type']
    self.path = dict['path']
    self.gui_type = dict['gui_type']
    self.description = dict['description']
    self.links = {}

  #TODO: Maybe put this functionality in Controller?
  # def load_links(self):
    if self.type == 'link':
      self.links[self.dict['link_name']] = self.path
    elif self.type == 'link_folder':
      for link in os.listdir(self.path): 
        link_name = link #TODO: probably need to fix this
        self.links[link] =os.path.join(self.path, link_name)
    elif self.type == 'link_list':
      with open(self.path, 'r') as config_file:
        link_dict = yaml.safe_load(config_file)
        for key, value in link_dict.items():
          self.links[key] = value
    else:
      raise "invalid type of LinkGroup"

  
