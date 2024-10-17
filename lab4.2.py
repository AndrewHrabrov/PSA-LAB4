import os

def file_n_folders(dir_name):
    if not os.path.isdir(dir_name):
        print(f"Каталог '{dir_name}' не существует.")
        return 1

    return tuple(os.listdir(os.path.abspath(dir_name)))

