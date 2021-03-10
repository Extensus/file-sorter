import os
import collections
from pprint import pprint
from file_sorter_class import *

sorter = file_sorter_class()


sorter.map_files()
sorter.send_files_to_dirs()
