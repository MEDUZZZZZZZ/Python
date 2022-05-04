# 5. Задан список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
# Техническое задание
#
# Здесь нет условия создавать итератор/генератор или comprehensions.
# Сохранение исходного порядка в результирующем списке обязательно.
# Не используйте Counter из модуля collections или аналогичные.
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#Через цикл

result =[]
for numbers in src:
    if src.count(numbers) == 1:
        result.append(numbers)
    else:
        continue
print(f'Решение через цикл: {result}')
# Через comprehensions

result =  [number for number in src if src.count(number) == 1]
print(f'Решение через comprehensions: {result}')


