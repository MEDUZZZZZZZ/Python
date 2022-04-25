# 4 [Задача со звездочкой]: усложненный вариант задания 3. Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
# Условие задачи
# Техническое задание
# Количество передаваемых строк в функцию может быть любым. Считаем, что переданы будут только корректные строки.
# Вернуть словарь, с ключами, отсортированными в алфавитном порядке.
# Усложнение:
#
# Поменяйте местами фамилию и имя в строках. Т.е. вместо 'Петр Алексеев' в конечный словарь вносить 'Алексеев Петр'
# Это преобразование не должно потребовать дополнительного прохода по словарю или списку параметров.
def thesaurus_adv(*args):
    big_dict = {}
    for item in args:
        secondname_first_letter = (item.split(' '))[1][0]
        if secondname_first_letter in big_dict:
            big_dict[secondname_first_letter].append(item)
            # element = big_dict.get(secondname_first_letter)
            # element.append(item)
            # big_dict[secondname_first_letter] = element
        else:
            big_dict[secondname_first_letter] = [item]
    for key, item in big_dict.items():
        small_dict = {}
        for name in sorted(item):
            firstname_letter = name[0]
            for_assigment = name.split(' ')
            name = f'{for_assigment[1]} {for_assigment[0]}'
            if firstname_letter in small_dict:
                small_dict[firstname_letter].append(name)
                # element = small_dict.get(firstname_letter)
                # element.append(name)
                # small_dict[firstname_letter] = [element]
                big_dict[key] = dict(sorted(small_dict.items()))
            else:
                small_dict[firstname_letter] = [name]
                big_dict[key] = dict(sorted(small_dict.items()))
    return dict(sorted(big_dict.items()))

dict_test = thesaurus_adv(
            "Таисия Тимофеева", "Артём Колосов", "Михаил Новиков", "Богдан Фролов", "Полина Колесникова",
            "Артём Агафонов", "Ева Шубина", "Даниил Зубков", "Фёдор Федоров", "Проскофья Ксенофонтовна",
            "Алиса Алексеева", "Олег Попов", "Вероника Маркова", "Кира Швецова","Нина Литвинова",
            "Оливия Филиппова", "Марта Богданова", "Дмитрий Зотов", "Анна Максимова", "Лев Овсянников",
            "Павел Сидоров", "Ирина Плотникова", "Полина Денисова", "Кирилл Иванов", "Максим Покровский")
print('{')
for key, item in dict_test.items():
    text = f'    "{key}":'
    text += '{'
    print(text)
    count = 1
    for key, element in item.items():
        if count == len(item):
            text = f'        "{key}": {element}'
            text += '}'
            print(text)
        else:
            count += 1
            text = f'        "{key}": {element}'
            print(text)
print('}')
