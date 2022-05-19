import  pathlib
import  json
path_file_1 = pathlib.Path('Files', 'task_3_users.csv')
path_file_2 = pathlib.Path('Files', 'task_3_hobby.csv')
path_result = pathlib.Path('Files', 'task_6_3_result.txt')
path_result_json = pathlib.Path('Files', 'task_6_3_result.json')
list_of_id =[]
list_of_hobby =[]
dict_users_hobby = {}
with open(path_file_1, mode='rt', encoding='utf-8') as users_file:
    for line in users_file:
        line = line.strip()
        name,second_name, patronymic = line.split(',')
        id = f'{name[0]}{second_name[0]}{patronymic[0]}'
        list_of_id.append(id)
len_id = len(list_of_id)-1
with open(path_file_2, mode='rt', encoding='utf-8') as hobby_file:
    for line in hobby_file:
        line = line.strip().replace(',', ';')
        list_of_hobby.append(line)
len_hobby  = len(list_of_hobby)-1
with  open(path_result_json, mode='wt',encoding='utf-8') as json_file:
    with open(path_result, mode='wt', encoding='utf-8') as f:
        if len_id == len_hobby:
            for id in list_of_id:
                dict_users_hobby[id] = list_of_hobby[list_of_id.index(id)]
        elif len_id > len_hobby:
            for id in list_of_id:
                if list_of_id.index(id) <= len_hobby:
                    dict_users_hobby[id] = list_of_hobby[list_of_id.index(id)]
                elif list_of_id.index(id) > len_hobby:
                    dict_users_hobby[id] = None
        else:
            for id in list_of_id:
                dict_users_hobby[id] = list_of_hobby[list_of_id.index(id)]
            f.writelines(str(dict_users_hobby))
            json_str = json.dumps(dict_users_hobby, indent=4, ensure_ascii=False)
            json_file.write(json_str)
            exit(1)
        f.writelines(str(dict_users_hobby))
        json_str = json.dumps(dict_users_hobby, indent=4, ensure_ascii=False)
        json_file.write(json_str)

























# # import  pathlib
# path_file_1 = pathlib.Path('Files', 'task_3_users.csv')
# path_file_2 = pathlib.Path('Files', 'task_3_hobby.csv')
# list_of_id = []
# list_of_hobby = []
# final_dict = {}
# with open(path_file_1, mode='r', encoding='utf-8') as users_file:
#     users_content_raw = users_file.readlines()
#     for users in users_content_raw:
#         second_name, first_name, patronimyc = users.strip().split(',')
#         id = f'{second_name[0]}{first_name[0]}{patronimyc[0]}'
#         list_of_id.append(id)
# len_id = len(list_of_id)
# with open(path_file_2, mode='r', encoding='utf-8') as hobby_file:
#     hobby_conten_raw = hobby_file.readlines()
#     for hobby in hobby_conten_raw:
#         hobby = hobby.strip().replace(',', ';')
#         list_of_hobby.append(hobby)
# len_hobby = len(list_of_hobby)
# for id in list_of_id:
#     if len_id ==




