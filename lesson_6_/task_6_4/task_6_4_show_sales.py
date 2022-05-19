from sys import argv
import pathlib
path_file = pathlib.Path('..', 'Files', 'bakery.cvs')


def show_sales(value=None):
    with open(path_file, mode='rt', encoding='utf-8') as f:
        if value:
            if len(value) == 1:
                content = f.read()
                return content
            elif len(value) == 2 and value[1].isdigit():
                start = int(value[1]) - 1
                for i in range(start):
                    f.readline()
                content = f.read()
                return content
            elif len(value) == 3 and value[1].isdigit() and value[2].isdigit():
                content = f.readlines()
                result = ''
                for line in content[int(value[1])-1:int(value[2])]:
                    result += f'{line}'
                return result
            elif value[1].isdigit() is False or value[2].isdigit() is False:
                return 'Параметры можно вводить только в числовом формате'
            else:
                return 'Введено слишком много параметров'


print(show_sales(argv))
