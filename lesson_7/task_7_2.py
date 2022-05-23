from pathlib import Path
import shutil
config_path = Path('.','Files','config_2.yaml')
first_nesting_level = '  - ' # попробовать через count
second_nesting_level = '    - '
third_nesting_level = '      - '
fourth_nesting_level = '        - '
nesting_symbol = '- '
with open(config_path, mode='rt', encoding='utf-8') as config_file:
    for line in config_file:
        line = line.replace('\n','')
        cur_nesting_level = line.count(' ')
        if line[-1] == ':':
            if not line.startswith(' '):
                dir_name = line.split(':')[0]
                mother_dir_path = Path('.', 'task_7_2', dir_name)
                Path(mother_dir_path).mkdir(parents=True, exist_ok=True)
            elif line.startswith(first_nesting_level):
                previous_nesting_level = line.count(' ')
                dir_name = line.split(first_nesting_level)[1].split(':')[0]
                first_nesting_level_path = Path(mother_dir_path, dir_name)
                Path(first_nesting_level_path).mkdir(parents=True, exist_ok=True)
            elif line.startswith(second_nesting_level):
                dir_name = line.split(second_nesting_level)[1].split(':')[0]
                second_nesting_level_path = Path(first_nesting_level_path, dir_name)
                Path(second_nesting_level_path).mkdir(parents=True, exist_ok=True)
            elif line.startswith(third_nesting_level):
                dir_name = line.split(third_nesting_level)[1].split(':')[0]
                third_nesting_level_path = Path(second_nesting_level_path,dir_name)
                Path(third_nesting_level_path).mkdir(parents=True, exist_ok=True) #Попробовать вынести в конец скрипта
            else:
                print("Неопределен уровень вложенности")
        else:
            if line.startswith(first_nesting_level):
                file_name = line.split(first_nesting_level)[1]
                file_path = Path(mother_dir_path, file_name)
            elif line.startswith(second_nesting_level):
                file_name = line.split(second_nesting_level)[1]
                file_path = Path(first_nesting_level_path, file_name)
            elif line.startswith(third_nesting_level):
                file_name = line.split(third_nesting_level)[1]
                file_path = Path(second_nesting_level_path, file_name)
            elif line.startswith(fourth_nesting_level):
                file_name = line.split(third_nesting_level)[1]
                file_path = Path(third_nesting_level_path, file_name)
            file_path.touch()  # можно вынести  в конец скрипта
