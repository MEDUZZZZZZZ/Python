# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.
# Условие задачи
# Техническое задание:
#
# duration - целое число: время в секундах. Вы можете вводить duration с клавиатуры или сразу занести в код.
# Формат вывода результата:
#
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input('Введите время в секундах: '))
if 0 < duration < 60:
    print('Осуществляем пересчет')
    print(f'{duration} сек')
elif duration < 3600:
    minutes = duration // 60
    sec = duration % 60
    print('Осуществляем пересчет')
    print(f'{minutes} мин {sec} сек')
elif duration < 86400:
    hours = duration // 3600
    sec_left = duration % 3600
    minutes = sec_left // 60
    sec = sec_left % 60
    print('Осуществляем пересчет')
    print(f'{hours} час {minutes} мин {sec} сек')
else:
   days = duration // 86400
   sec_left = duration % 86400
   hours = sec_left // 3600
   sec_left_1 = sec_left % 3600
   minutes = sec_left_1 // 60
   sec = sec_left_1 % 60
   print('Осуществляем пересчет')
   print(f'{days} дн {hours} час {minutes} мин {sec} сек')
