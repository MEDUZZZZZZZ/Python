from pathlib import Path
config_path = Path('.', 'Files', 'config_2.yaml')
nesting_symbol = '- '
with open(config_path, mode='rt', encoding='utf-8') as config_file:
    for line in config_file:
        line = line.replace('\n', '')
        cur_nest = line.split(nesting_symbol)[0].count(' ')
        if not cur_nest:
            prev_nest = cur_nest
            if line[-1] == ':':
                dir_name  = line.split(':')[0]
                path = Path('task_7_2_2', dir_name)
                Path(path).mkdir(parents=True, exist_ok=True)
            else:
                file_name = line
                path = Path('task_7_2_2', file_name)
                path.touch()
        elif  cur_nest > prev_nest:
            prev_nest = cur_nest
            if line[-1] == ':':
                dir_name = line.split(':')[0].split(nesting_symbol)[1]
                path = Path(path, dir_name)
                Path(path).mkdir(parents=True, exist_ok=True)
            else:
                file_name = line.split(nesting_symbol)[1]
                path = Path(path, file_name)
                path.touch()
        elif cur_nest < prev_nest:
            counter = (prev_nest - cur_nest)//2
            prev_nest = cur_nest
            if line[-1] == ':':
                dir_name = line.split(':')[0].split(nesting_symbol)[1]
                for level in range(counter+1):
                    path = Path(path.parent)
                path = Path(path,dir_name)
                Path(path).mkdir(parents=True, exist_ok=True)
            else:
                file_name = line.split(nesting_symbol)[1]
                for level in range(counter+1):
                    path = Path(path.parent)
                path = Path(path, file_name)
                path.touch()
        elif cur_nest == prev_nest:
            if line[-1] == ':':
                dir_name = line.split(':')[0].split(nesting_symbol)[1]
                path = Path(path.parent, dir_name)
                Path(path).mkdir(parents=True, exist_ok=True)
            else:
                file_name = line.split(nesting_symbol)[1]
                path = Path(path.parent, file_name)
                path.touch()
