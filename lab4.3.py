import os
from inspect import stack


def dir_tree(dir_name):
    stack = [(dir_name, 0)]

    while stack:
        cur_dir, level = stack.pop()
        elements = os.listdir(cur_dir)
        files = ()
        for elem in elements:
            path = os.path.join(cur_dir, elem)
            if os.path.isdir(path): stack.append((path, level + 1))
            if os.path.isfile(path):
                indent = (4 * level) * ' '
                print(indent + elem)


