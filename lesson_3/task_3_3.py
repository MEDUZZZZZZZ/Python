def thesaurus(*args):
    names_dict = {}
    for i in args:
        first_letter = i[0]
        if first_letter in names_dict:
            names_dict[first_letter].append(i)
            # element = names_dict.get(first_letter)
            # element.append(i)
            # names_dict[first_letter] = element
        else:
            names_dict[first_letter] = [i]
    return dict(sorted(names_dict.items()))
dict_test = thesaurus(
    'Олег', "Артем",
    "Сергей", "Константин",
    "Ольга", "Алексей",
    "Игорь", "Евдокия",
    "Джон", "Савелий",
    "Ян")
print('{')
for key, item in dict_test.items():
    print(f'    "{key}": {item}')
print('}')

