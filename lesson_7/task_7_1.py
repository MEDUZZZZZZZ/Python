from pathlib import Path
dir_for_previous_project_path = Path('.','task_7_1', 'old_project')
mother_dir_path = Path('.','task_7_1', 'my_project')
# Решение строго по ТЗ
list_of_dir_names = ['settings', 'mainapp', 'adminapp', 'authapp']
if not mother_dir_path.exists():
    for dir_name in list_of_dir_names:
        dir_path = Path(mother_dir_path, dir_name)
        Path(dir_path).mkdir(parents=True)
else:
    Path(dir_for_previous_project_path).mkdir()
    for dir_name in list_of_dir_names:
        dir_path = Path(mother_dir_path, dir_name)
        if dir_path.exists():
            new_path = Path(dir_for_previous_project_path, dir_name)
            Path(dir_path).rename(new_path)
            Path(dir_path).mkdir(parents=True)
        else:
            Path(dir_path).mkdir(parents=True)

