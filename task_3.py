import os
from shutil import copy2

tmplt_dir = os.path.join('my_project', 'templates')
try:
    os.mkdir(tmplt_dir)
except FileExistsError as e:
    pass

for r, d, f in os.walk('my_project'):
    if 'templates' in r and tmplt_dir not in r:
        if 'templates' in os.path.basename(r):
            for dir_name in d:
                os.makedirs(os.path.join(tmplt_dir, dir_name), exist_ok=True)
        else:
            for file_name in f:
                if file_name.endswith('.html'):
                    src_dir = r.split('templates')[1].lstrip(os.path.sep)

                    copy2(os.path.join(r, file_name), os.path.join(tmplt_dir, src_dir))