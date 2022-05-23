from pathlib import Path
from os import walk, stat
import json
data_path = Path('.','task_7_5', 'some_data_adv')
dict_of_files = {10**power:[0,[]] for power in range(2,7)}
for  root, dirs, files in walk(data_path):
    counter  =  0
    for file in files:
        counter += 1
        file_path = Path(data_path, file)
        file_size = stat(file_path)[6]
        file_ext = file.split('.')[1]
        for keys in dict_of_files:
            if file_size < keys:
                dict_of_files[keys][0] += 1
                if not file_ext in dict_of_files[keys][1]:
                    dict_of_files[keys][1].append(file_ext)
                break
print(counter)
with open('task_7_5_summary.json', mode='wt',encoding='utf-8') as file:
    json_str = json.dumps(dict_of_files, ensure_ascii=False)
    file.write(json_str)
text = '{'
for  key, value in dict_of_files.items():
    text += f'{key}: {value}\n'
text += '}'
print(text)