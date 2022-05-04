# 3. Реализовать склонение слова «процент» во фразе «N процентов».
# Условие задачи
# Техническое задание:
#
# Вывести фразу «N процентов» с правильным склонением слова процент на экран отдельной строкой для каждого из чисел в интервале от 1 до 101.
# Ваш алгоритм должен корректно работать для всех чисел интервала от 1 до 101.
# Правила склонения здесь достаточно просты: всего три варианта: «процент»/«процента»/«процентов».
# Формат вывода результата:
#
# 0 процентов
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов
# 101 процент
# Усложнение:
#
# Сделайте эту же задачу для интервала от 1 до 200. Подумайте над тем почему такая задача - усложненная? В чем сложность?

print("Я научился склонять проценты")
percent = None
for percent in range(1, 201):
    if_tens = percent % 10
    if_hundreds = percent % 100
    if if_hundreds % 100 in range(11, 15) or if_tens in range(5, 10) or if_tens == 0:
        print(f'{percent} процентов')
    elif if_tens in range(2, 5):
        print(f'{percent} процента')
    else:
        print(f'{percent} процент')