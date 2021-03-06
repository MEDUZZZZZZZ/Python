# 2. Для кубов нечётных чисел от 1 до 1000. Вычислить сумму чисел, сумма цифр кубов которых делится нацело на 7.
# Условие задачи
# Техническое задание:
#
# Для всех нечетных чисел диапазона [1, 1000]
# вычислить их куб
# вычислить сумму цифр куба
# если сумма цифр куба делится нацело на 7, то добавить в накопительную сумму исходное число.
# При решении задачи использовать только арифметические операции и цикл while.
# Не используем списки, функцию range, преобразование числа в строку/список.
# Ваш алгоритм должен корректно работать для всех чисел интервала от 1 до 1000, но и легко изменяться для другого диапазона чисел, например от 1 до 10000000.
# Формат вывода результата:
# Вывод на экран формить в виде: число ^3 = куб_числа; [сумма цифр куба] накопительная_сумма
# Например:
#
# 19 ^3 = 6859 [ 28 ] накоп. сумма: 19
# 31 ^3 = 29791 [ 28 ] накоп. сумма: 50
# 43 ^3 = 79507 [ 28 ] накоп. сумма: 93
# 49 ^3 = 117649 [ 28 ] накоп. сумма: 142
# 53 ^3 = 148877 [ 35 ] накоп. сумма: 195
# 55 ^3 = 166375 [ 28 ] накоп. сумма: 250
# ...
# 967 ^3 = 904231063 [ 28 ] накоп. сумма: 43106
# Примечание:
# число 19, 19 ^ 3 = 6859, сумма чисел 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Поэтому 19 включаем в вывод.
# Сумма считается для самих чисел 19, 31, 43 и т.п. Не для кубов.
number = 1
numbers_sum = 0
while number < 1001:
    if number % 2 != 0:
        cube = number**3
        copy_of_cube = cube
        counter = 0
        while copy_of_cube != 0:
            copy_of_cube = copy_of_cube // 10
            counter += 1
        copy_of_cube = cube
        digits_sum = 0
        while counter != 0:
            counter -= 1
            qube_digit = copy_of_cube // (10**counter)
            copy_of_cube = copy_of_cube % (10**counter)
            digits_sum += qube_digit
        if digits_sum % 7 == 0:
            numbers_sum += number
            print(f'{number}^3 = {cube} [{digits_sum}] накоп. сумма: {numbers_sum}')
        number += 1
    else:
        number += 1
