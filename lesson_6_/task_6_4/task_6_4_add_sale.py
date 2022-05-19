from sys import argv
import pathlib
path_file = pathlib.Path('..', 'Files', 'bakery.cvs')


def add_sale(value):
    with open(path_file, mode='at', encoding='utf-8') as f:
            f.write(value[1])
            f.write('\n')


if len(argv) == 1 or len(argv) > 2:
    print('Вы ввели неверное количество параметров')
elif len(argv) == 2 and argv[1].isdigit():
    add_sale(argv)
else:
    print('Введены данные неверного формата')

