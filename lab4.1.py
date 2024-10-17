import os
import shutil
from shutil import copytree, ignore_patterns


def unpck(arh_name, extract_dir='master', copy_dir='copy', mask='*'):
    os.path.abspath(extract_dir)
    os.path.abspath(copy_dir)
    shutil.unpack_archive(arh_name, extract_dir)

    os.makedirs(copy_dir, exist_ok=True)

    copytree(extract_dir, copy_dir, ignore=ignore_patterns(mask), dirs_exist_ok=True)
    archive_path = os.path.join(os.path.dirname(arh_name),
                                'copyof_' + os.path.basename(arh_name).replace('.tar.gz', ''))
    shutil.make_archive(archive_path, 'gztar', copy_dir)



