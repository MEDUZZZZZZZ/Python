# 6. [Задача со звездочкой]: усложненный вариант задания 5.
# Условие задачи
# Техническое задание
# 
# Добавьте в функцию еще один аргумент, разрешающий или запрещающий повторы слов в шутках: 
# каждое слово можно использовать только в одной шутке. Тогда этот параметр логично сделать типом boolean.
# Функция должна вернуть список строк-шуток сколько потребовали или сколько получилось из условия уникальности.
# Проверьте работу функции для разного количества шуток. Убедитесь в том, что каждое слово встречается только один раз.

import random
# Cоставные части шуток по ТЗ

actors = ["автомобиль", "лес", "огонь", "город", "дом"]
setups = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
punchlines = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# Составные части шуток для генерации анекдотов категории Б

# actors = ["Медведь", "Мужик", "Петька", "Мусятник", "Улитка"]
# setups = ["надел шляпу", "сел в горящую машину", "задал вопрос Васильевичу", "купи слона", "заходит в бар"]
# punchlines = ["а она ему как раз", "и сгорел", "но есть один нюанс", "а ты возьми и купи слона",
# "возвращается через неделю и говорит: зачем ты это сделал?"]

def get_jokes_adv(count, actors, setups, punchlines, repetition):
    """
     Generate the selected number of perfect 'category b' jokes from components
     in 3 different lists with option to turn off the repetition of words
    """
    actors = actors[:]
    setups = setups[:]
    punchlines = punchlines[:]
    list_of_jokes = []
    i = 0
    if repetition:
        while i is not count:
            text = f'{random.choice(actors)} {random.choice(setups)} {random.choice(punchlines)}'
            list_of_jokes.append(text)
            i += 1
    else:
        if count > len(actors) or count > len(setups) or count > len(punchlines):
            print('Не могу придумать особенную шутку')
        else:
            while i is not count:
                actor = actors.pop(random.randint(0, len(actors)-1))
                setup = setups.pop(random.randint(0, len(setups)-1))
                punchline = punchlines.pop(random.randint(0 ,len(punchlines)-1))
                text = f'{actor} {setup} {punchline}'
                list_of_jokes.append(text)
                i += 1
    return list_of_jokes
print("Если повторения исключены")
print()
list_for_ready_jokes = (get_jokes_adv(5, actors, setups, punchlines, False))
for index, element in enumerate(list_for_ready_jokes):
    print(f'Искрометная шутка № {index+1}: ')
    print(element)
    print()
print('Если потворения разрешены')
print()
list_for_ready_jokes = (get_jokes_adv(10, actors, setups, punchlines, True))
for index, element in enumerate(list_for_ready_jokes):
    print(f'Искрометная шутка № {index+1}: ')
    print(element)
    print()