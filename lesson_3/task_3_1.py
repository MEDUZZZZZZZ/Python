# 1. Написать функцию num_translate, переводящую числительные от 0 до 10 c английского на русский язык.
# Условие задачи
# Техническое задание
# 
# Функция num_translate возвращает строку перевод. Или возвращает None, если перевести невозможно. 
# Обратите внимание, что возвращается None как объект, а не как строка "None". 
# Не путайте печать значения (print) и его возврат из функции (return).
# Функция принимает параметр - строку слово для перевода, и другие параметры, если нужно - по вашему усмотрению. 
# В примере специально они не указаны.
# Здесь нет требований на регистр входного слова. Возвращается результат в нижнем регистре.
# Выполнить вызов функции для нескольких слов и вывести на экран результаты.

dictionary = {
    'one': 'один', 'two': 'два',
    'three': 'три', 'four': 'четыре',
    'five': 'пять', 'six': 'шесть',
    'seven': 'семь', 'eight': 'восемь',
    'nine': 'девять', 'ten': 'десять'}
def num_translate(eng_num, my_dictionaty = dictionary):
    eng_num = eng_num.lower()
    translation = dictionary.get(eng_num)
    return translation
print(num_translate('One'))
print(num_translate('two'))
print(num_translate('THREE'))
print(num_translate('FOur'))
print(num_translate('FIVe'))
print(num_translate('sIX'))
print(num_translate('SeVeN'))
print(num_translate('Eight'))
print(num_translate('nine'))
print(num_translate('ten'))
print(num_translate('exit'), type(num_translate('exit')))