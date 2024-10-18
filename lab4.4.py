from pathlib import Path, PurePath


def find_expansion(dir_name, exp):
    dir_name = Path(dir_name).resolve()
    stack = [(dir_name)]
    files = []
    while stack:
        cur_dir = stack.pop()
        elements = Path(cur_dir).iterdir()
        for elem in elements:
            path = PurePath(cur_dir).joinpath(elem)
            if Path(path).is_file():
                expansion = PurePath(path).suffix
                if (expansion == exp):
                    files.append(Path(PurePath(path)).resolve().as_posix())
            if Path(path).is_dir(): stack.append(path)
    print(files)

find_expansion('master', '.html')