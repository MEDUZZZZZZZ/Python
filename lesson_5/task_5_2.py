# 2. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield.
# Полностью истощить генератор.
# Техническое задание
#
# Все пункты ТЗ задания 1 остаются в силе.
# Отличие от задания 1 - только в использовании yield.
# Усложнение [одна звездочка]:
# С ключевым словом yield - как в задании 1: генератор нечётных чисел от 1 до n (включительно),
# для чисел, квадрат которых меньше 200.
#
# Усложнение [две звездочки]:
# С ключевым словом yield: Вычислять и возвращать само число и накопительную сумму этого и предыдущих чисел.

# Через цикл for

def iterator_with_yeld_for(n):
    """Генератор через цикл for"""
    sum = 0
    for counter in range(n+1):
        if counter % 2 != 0 and counter**2 < 200:
            sum += counter
            yield counter, sum
        else:
            continue

gen1 = iterator_with_yeld_for(20)
for number_and_sum in gen1:
    print(number_and_sum)
next(gen1)

#  Решение через while
#
# def iterator_with_yeld_while(n):
#     """Генератор через цикл while"""
#     counter  = 1
#     sum = 0
#     while counter <= n:
#         if counter % 2 != 0 and counter**2 < 200:
#             sum += counter
#             yield counter, sum
#             counter += 1
#         else:
#             counter += 1
#             continue
#
# gen1 = iterator_with_yeld_while(20)
# for number_and_sum in gen1:
#     print(number_and_sum)
# next(gen1)
