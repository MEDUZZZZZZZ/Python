# 3. Есть два списка: tutors - имена учеников, groups - названия их классов.
# Необходимо реализовать генератор или функцию-генератор, возвращающий кортежи вида '(<tutor>, <group>)'.
# Техническое задание
#
# Функция (или генератор) должна работать со списками любой длины.
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке groups меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде:
# '(<tutor>, None)', например: '('Станислав', None)'
# Если в списке tutors меньше элементов, чем в списке groups, то смотри пункт 2.
# Генератор возвращает кортежи указанного вида.
# Доказать, что вы создали именно генератор. Вывести все его значения на экран.
# Не используйте в этом задании функции zip и zip_longest.
# Не меняйте исходные списки tutors и groups и не создавайте новых списков.
# Подтвердите работоспособность(выведите в консоль результаты) для обоих вариантов:
# groups меньше tutors и tutors меньше groups.
# Примечание:
# Сделать эту задачу через функцию-генератор проще.
# Если сделали, попробуйте сделать именно через генераторное выражение, т.е. «в одну строку».
def storing_gen(list1,list2):
    """ Возвращает генератор пар ученик группа """
    counter = 0
    for tutor in list1:
        if counter <= len(list2) - 1:
            yield tutor, list2[counter]
            counter += 1
        else:
            yield tutor, None

# Списки для случая если учеников меньше групп
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
groups = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
# Списки для случая если учеников больше групп
tutors1 = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
groups1 = [
    '9А', '7В', '9Б', '9В'
]

print(f'Решение если учеников меньше:\nУченики: {tutors}\nГруппы: {groups}')
gen1 = storing_gen(tutors, groups)
print(f'Тип объекта: {type(gen1)}\nВсе значения генератора:')
for couple in gen1:
    print(couple)
print()

print(f'Решение если учеников больше:\nУченики: {tutors1}\nГруппы: {groups1}')
gen1  = storing_gen(tutors1, groups1)
print(f'Тип объекта: {type(gen1)}\nВсе значения генератора:')
for couple in gen1:
    print(couple)