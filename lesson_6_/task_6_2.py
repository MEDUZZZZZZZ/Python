import pathlib
path_file = pathlib.Path('Files','nginx_logs.txt')
file = open(path_file,  mode = 'rt', encoding='utf-8')
required_list = []
list_of_adresses = []
dict_of_ip = {}
for line in file:
    line_content = line.split(' ')
    adress, typeee, action = line_content[0],  line_content[5][1:], line_content[6]
    content = adress, typeee, action
    required_list.append(content)
    if adress not in dict_of_ip:
        dict_of_ip[adress] = 1
    elif adress in dict_of_ip:
        dict_of_ip[adress] += 1
file.close()
print(required_list)
max_count = max(dict_of_ip.values())
spamer = {ip:count for ip, count in dict_of_ip.items() if count == max_count}
for k, v in spamer.items():
    print(f'IP адрес спамера: {k}, общее кол-во запросов: {v}')
