from active_file_sorter import *

# class assignment
sorter = file_sorter_class()

# maps all files in the directories specified in file_sort_var_db.txt
sorter.map_files()
# relocates/renames the files
sorter.send_files_to_dirs()
