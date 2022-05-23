from pathlib import Path
from os import walk, stat
data_path = Path('.','task_7_4', 'some_data')
dict_of_files = {10**power: 0 for power in range(2,6)}
for  root, dirs, files in walk(data_path):
    for file in files:
        file_path = Path(data_path, file)
        file_size = stat(file_path)[6]
        for keys in dict_of_files:
            if file_size < keys:
                dict_of_files[keys] += 1
                break
text = '{\n'
for key, value in dict_of_files.items():
    text += f'{key}: {value}\n'
text += '}'
print(text)




