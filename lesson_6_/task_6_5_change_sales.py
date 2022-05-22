import pathlib
from sys import argv
path_file = pathlib.Path('Files', 'bakery.cvs')


def change_sale(data):
    if len(data) == 3:
        index = int(data[1]) - 1
        new_sale = data[2]
        counter = 0
        if new_sale.isdigit():
            with open(path_file, mode='r+', encoding='utf-8') as sales_file:
                change = ''
                for sale in sales_file:
                    if counter != index:
                        change += sale
                        counter += 1
                    else:
                        replace = sale.replace(sale, f'{new_sale}\n')
                        change += replace
                        counter += 1
                sales_file.seek(0)
                sales_file.write(change)
            return 'Изменение прошло успешно'
        else:
            return 'Введеный аргумент должен быть целым положительным числом'
    else:
        return 'Передано неправильное количество парматеров'


print(change_sale(argv))
