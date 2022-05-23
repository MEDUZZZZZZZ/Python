from pathlib import Path
from os import walk
from shutil import copytree
path_resourse = Path('.', 'task_7_3', 'my_project')
path_new_templates = Path('.', 'task_7_3', 'my_project', 'templates')
for root, dirs, files in walk(path_resourse):
    try:
        if dirs.index('templates') >= 0:
            path_templates_1 = Path(root,'templates')
            copytree(path_templates_1,path_new_templates,dirs_exist_ok=True)
    except ValueError:
        continue
