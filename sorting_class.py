import os
import collections
import tree_dependency_class


class file_sort_instance():
    def generate_file_map(self, is_mapping, map, dir):
        if is_mapping:
            file_list = os.listdir(dir)
            for file_name in file_list:
                if file_name[0] != '.':
                    file_ext = file_name.split('.')[-1]
                    map[file_ext].append(file_name)

    def general_sorting_instance(self, map, init_dir, destination_dir, dir_list):
        for f_ext, f_list in map.items():
            for index, dir in enumerate(dir_list):
                if f_ext in self.EXT_AUDIO:
                    for file in f_list:
                        os.rename(os.path.join(init_dir, file), os.path.join(destination_dir, file))

''' if self.desktop_file_mapping:
        file_list = os.listdir(self.DESK_DIR)
        for file_name in file_list:
            if file_name[0] != '.':
                file_ext = file_name.split('.')[-1]
                self.desktop_file_map[file_ext].append(file_name)'''