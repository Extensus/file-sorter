import collections
from pprint import pprint
from datastack_handler import *


class file_sorter_class(object):
    api = databaseApi()
    fetchedVars = api.get_from_base()
    pprint(fetchedVars)

    EXT_AUDIO = fetchedVars['Audio Extensions']
    EXT_VIDEO = fetchedVars['Video Extensions']
    EXT_IMAGES = fetchedVars['Image Extensions']
    EXT_DOCS = fetchedVars['Document Extensions']
    EXT_COMPRESSED = fetchedVars['Compressed File Extensions']
    EXT_INSTALLATIONS = fetchedVars['Executable Extensions']

    EXT_WORD = fetchedVars['Word Extensions']
    EXT_PPP = fetchedVars['Power Point Extensions']

    DOWN_DIR = fetchedVars['Downloads Directory']
    DOC_DIR = fetchedVars['Documents Directory']
    DESK_DIR = fetchedVars['Desktop Directory']
    MUSIC_DIR = fetchedVars['Music Directory']
    VIDEO_DIR = fetchedVars['Video Directory']

    image_dir = fetchedVars['Pictures Directory']
    compressed_dir = fetchedVars['Zip File Directory']
    exe_dir = fetchedVars['Executable Directory']

    down_file_mapping = fetchedVars['Sort Downloads']
    down_file_map = collections.defaultdict(list)
    doc_file_mapping = fetchedVars['Sort Documents']
    doc_file_map = collections.defaultdict(list)
    desktop_file_mapping = fetchedVars['Sort Desktop']
    desktop_file_map = collections.defaultdict(list)
    audio_file_mapping = fetchedVars['Sort Audio']
    audio_file_map = collections.defaultdict(list)
    video_file_mapping = fetchedVars['Sort Video']
    video_file_map = collections.defaultdict(list)

    def map_files(self):
        try:
            if self.down_file_mapping:
                file_list = os.listdir(self.DOWN_DIR)
                for file_name in file_list:
                    if file_name[0] != '.':
                        file_ext = file_name.split('.')[-1]
                        self.down_file_map[file_ext].append(file_name)

            if self.doc_file_mapping:
                file_list = os.listdir(self.DOC_DIR)
                for file_name in file_list:
                    if file_name[0] != '.':
                        file_ext = file_name.split('.')[-1]
                        self.doc_file_map[file_ext].append(file_name)

            if self.desktop_file_mapping:
                file_list = os.listdir(self.DESK_DIR)
                for file_name in file_list:
                    if file_name[0] != '.':
                        file_ext = file_name.split('.')[-1]
                        self.desktop_file_map[file_ext].append(file_name)

            if self.audio_file_mapping:
                file_list = os.listdir(self.MUSIC_DIR)
                for file_name in file_list:
                    if file_name[0] != '.':
                        file_ext = file_name.split('.')[-1]
                        self.audio_file_map[file_ext].append(file_name)

            if self.video_file_mapping:
                file_list = os.listdir(self.VIDEO_DIR)
                for file_name in file_list:
                    if file_name[0] != '.':
                        file_ext = file_name.split('.')[-1]
                        self.video_file_map[file_ext].append(file_name)

        except IndexError:
            print(f"No such directory (root = %s" % self.DOWN_DIR)

    def send_files_to_dirs(self):
        try:
            if self.down_file_mapping:
                for f_ext, f_list in self.down_file_mapping.items():
                    if f_ext in self.EXT_AUDIO:
                        for file in f_list:
                            os.rename(os.path.join(self.DOWN_DIR, file), os.path.join(self.MUSIC_DIR, file))

                    elif f_ext in self.EXT_VIDEO:
                        for file in f_list:
                            os.rename(os.path.join(self.DOWN_DIR, file), os.path.join(self.VIDEO_DIR, file))

                    elif f_ext in self.EXT_IMAGES:
                        for file in f_list:
                            os.rename(os.path.join(self.DOWN_DIR, file), os.path.join(self.image_dir, file))

                    elif f_ext in self.EXT_DOCS:
                        for file in f_list:
                            os.rename(os.path.join(self.DOWN_DIR, file), os.path.join(self.DOC_DIR, file))

                    elif f_ext in self.EXT_COMPRESSED:
                        for file in f_list:
                            os.rename(os.path.join(self.DOWN_DIR, file), os.path.join(self.compressed_dir, file))

                    elif f_ext in self.EXT_INSTALLATIONS:
                        for file in f_list:
                            os.rename(os.path.join(self.DOWN_DIR, file), os.path.join(self.exe_dir, file))

                    else:
                        pass
            else:
                pass

            if self.desktop_file_mapping:
                for f_ext, f_list in self.desktop_file_map.items():
                    if f_ext in self.EXT_AUDIO:
                        for file in f_list:
                            os.rename(os.path.join(self.DOWN_DIR, file), os.path.join(self.MUSIC_DIR, file))

                    elif f_ext in self.EXT_VIDEO:
                        for file in f_list:
                            os.rename(os.path.join(self.DOWN_DIR, file), os.path.join(self.VIDEO_DIR, file))

                    elif f_ext in self.EXT_IMAGES:
                        for file in f_list:
                            os.rename(os.path.join(self.DOWN_DIR, file), os.path.join(self.image_dir, file))

                    elif f_ext in self.EXT_DOCS:
                        for file in f_list:
                            os.rename(os.path.join(self.DOWN_DIR, file), os.path.join(self.DOC_DIR, file))

                    elif f_ext in self.EXT_COMPRESSED:
                        for file in f_list:
                            os.rename(os.path.join(self.DOWN_DIR, file), os.path.join(self.compressed_dir, file))

                    elif f_ext in self.EXT_INSTALLATIONS:
                        for file in f_list:
                            os.rename(os.path.join(self.DOWN_DIR, file), os.path.join(self.exe_dir, file))

                    else:
                        pass
            else:
                pass

            if self.doc_file_mapping:
                for f_ext, f_list in self.doc_file_mapping.items():
                    if f_ext == 'pdf':
                        for file in f_list:
                            destination = "PDF\\%s" % file
                            os.rename(os.path.join(self.DOC_DIR, file), os.path.join(self.DOC_DIR, destination))

                    elif f_ext in self.EXT_WORD:
                        for file in f_list:
                            destination = "Word\\%s" % file
                            os.rename(os.path.join(self.DOC_DIR, file), os.path.join(self.DOC_DIR, destination))

                    elif f_ext == 'txt':
                        for file in f_list:
                            destination = "TXT\\%s" % file
                            os.rename(os.path.join(self.DOC_DIR, file), os.path.join(self.DOC_DIR, destination))

                    else:
                        pass
            else:
                pass

            if self.audio_file_mapping:
                for f_ext, f_list in self.audio_file_map.items():
                    if f_ext in self.EXT_AUDIO:
                        for file in f_list:
                            destination = f"Audio\\%s" % file
                            os.rename(os.path.join(self.MUSIC_DIR, file), os.path.join(self.MUSIC_DIR, destination))

                    elif f_ext in self.EXT_VIDEO:
                        for file in f_list:
                            destination = f"Video\\%s" % file
                            os.rename(os.path.join(self.VIDEO_DIR, file), os.path.join(self.VIDEO_DIR, destination))

                    else:
                        pass
            else:
                pass
            
            if self.video_file_mapping:
                for f_ext, f_list in self.video_file_map.items():
                    if f_ext in self.EXT_AUDIO:
                        for file in f_list:
                            destination = f"Audio\\%s" % file
                            os.rename(os.path.join(self.MUSIC_DIR, file), os.path.join(self.MUSIC_DIR, destination))

                    elif f_ext in self.EXT_VIDEO:
                        for file in f_list:
                            destination = f"Video\\%s" % file
                            os.rename(os.path.join(self.VIDEO_DIR, file), os.path.join(self.VIDEO_DIR, destination))

                    else:
                        pass
            else:
                pass

        except FileExistsError:
            pass


if __name__ == '__main__':
    dir_sorting = file_sorter_class()

    print(dir_sorting.EXT_AUDIO)
