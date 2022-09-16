import pathlib
path_file = pathlib.Path('Files','nginx_logs.txt')
file = open(path_file,  mode = 'rt', encoding='utf-8')
required_list = []
d = {}
for line in file:
    line_content = line.split(' ')
    adress, typeee, action = line_content[0],  line_content[5][1:], line_content[6]
    content = adress, typeee, action
    required_list.append(content)
file.close()
print(required_list)




