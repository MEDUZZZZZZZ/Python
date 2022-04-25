# 2. [Задача со звездочкой]: усложненный вариант задания 1. Написать функцию num_translate_adv, 
# корректно обработает числительные, начинающиеся с заглавной буквы. 
# Если перевод сделать невозможно, вернуть объект None.
# Условие задачи
# Техническое задание
# 
# Функция возвращает строку перевод. Или возвращает None, если перевести невозможно.
# Считаем, что только первая буква может быть заглавной.
# Обратите внимание, что функция возвращает перевод в том же регистре как и приняла.
# Выполнить вызов функции для нескольких слов и вывести на экран результаты.
dictionary = {
    'one': 'один', 'two': 'два',
    'three': 'три', 'four': 'четыре',
    'five': 'пять', 'six': 'шесть',
    'seven': 'семь', 'eight': 'восемь',
    'nine': 'девять', 'ten': 'десять'}
def num_translate_adv(eng_num, my_dictionaty = dictionary):
    if eng_num == eng_num.capitalize():
        eng_num = eng_num.lower()
        translation = dictionary.get(eng_num)
        return translation.capitalize()
    else:
        translation = dictionary.get(eng_num)
        return translation
print(num_translate_adv('one'))
print(num_translate_adv('One'))
print(num_translate_adv('THREE'))
print(num_translate_adv('FOur'))
print(num_translate_adv('FIVe'))
print(num_translate_adv('sIX'))
print(num_translate_adv('SeVeN'))
print(num_translate_adv('Eight'))
print(num_translate_adv('nine'))
print(num_translate_adv('ten'))
print(num_translate_adv('exit'), type(num_translate_adv('exit')))