import os
import platform

def open_shortcut(shortcut_path, gui):
  try:
    gui.close_gui()
  except:
    pass

  operating_system = platform.platform()
  if 'macOS' in operating_system:
    os.system(f"open '{shortcut_path}'")
  else:
    os.startfile(shortcut_path) #TODO: fix this to based on absolute/relative path inputs
