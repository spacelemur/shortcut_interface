# Notes:

# Working:
  - group_link buttons
  - group_link_list buttons

# TODO list:
  [x] Figure out a way to close gui after following the shortcut
    - Note: this works, but this perhaps isn't the best way- passing GUI all the way down to the method. 
  [x] Implement something similar to the src/group_link_folder method of destroying main gui window to close
  [ ] For some reason Aliases don't work on MacOS - they open in Terminal.. Otherwise this works


  ## Link Folders:
    [x] the group_link_folder combobox option doesn't work
    [x] The combobox options are all mangled
    [x] For some reason there is no name around the frame
  
  ## Gui
    [x] Frames are all stacked on top of each other- looks bad and is disorganized
    [x] gui doesn't quit after it has finished doing what it's supposed to do
    - GroupLinkFolder
      [x]Key error if item isn't selected

  ## Improve layout
    [ ] Be able to create a grid of groups, either row or column and have gui populate max row after max
        # of columns or rows are reached. 


  ## Future plans:
    [ ] Would be nice to have a list with checkboxes - select which ones you want to open then to go 
    [ ] Drop down to select group then have buttons populate below depending on which group is selected
