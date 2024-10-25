import os
from os import listdir
from os.path import abspath, isdir


def file_n_folders(dir_name):
   path = abspath(dir_name)
   lsdirs = os.listdir(path)
   files = tuple(f for f in lsdirs if os.path.isfile(path + '/' + f))
   dirs = tuple(f for f in lsdirs if os.path.isdir(path + '/' + f))
   return [files, dirs]

