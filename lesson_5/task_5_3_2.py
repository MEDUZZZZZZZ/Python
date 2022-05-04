def storing_gen_adv(list1,list2):
    """ Возвращает генератор пар ученик, группа через генераторное выражение """
    result_gen = ((i, list2[list1.index(i)]) if list1.index(i) <= len(list2) - 1 else (i, None) for i in list1)
    return result_gen
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
gen1 = storing_gen_adv(tutors, groups)
print(f'Тип объекта: {type(gen1)}\nВсе значения генератора:')
for couple in gen1:
    print(couple)
print()

print(f'Решение если учеников больше:\nУченики: {tutors1}\nГруппы: {groups1}')
gen1  = storing_gen_adv(tutors1, groups1)
print(f'Тип объекта: {type(gen1)}\nВсе значения генератора:')
for couple in gen1:
    print(couple)
