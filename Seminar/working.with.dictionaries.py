# Работа со словарями
# 
my_dict = {"V": 23, "VX": 56, "VI": 90, "VI": 34, "VII": 123}

# print(my_dict)                      # Выводит словарь на экран
# print(my_dict.keys())               # Выводит на экран только ключи в виде вроде списка, но как в списке работать по индексами он не будет. 
#                                     # Можно работать с такими функциями как summ или len   
# print(len(my_dict.keys()))          # Длина ключей библиотеки
# print(list(my_dict.keys())[2])      # Преобразовываем библиотеку в список и выводим на экран ключ под вторым индексом
# print(my_dict.values())             # Выводит на экран только значания в виде вроде списка, но как в списке работать по индексами он не будет. 
#                                     # Можно работать с такими функциями как summ или len   
# print(sum(my_dict.values()))        # Вывели на экран сумму значении библиотеки
# print(my_dict.items())              # Выводит на экран список кортежей. Его можео всегда преобразовать в библиотеку.

# print('\n')
# for key in my_dict:                 # Проходим в цикле по ключам в библиотеке
#     print(key, end=' ')

# print('\n')
# for key in my_dict.keys():          # Проходим в цикле по ключам в библиотеке. Тоже самое что и предыдущая запись 
#     print(key, end=' ')
    
# print('\n')
# for value in my_dict.values():      # Проходим в цикле по значениям в библиотеке
#     print(value, end=' ')

# print('\n')
# for items in my_dict.items():       # Проходим в циклн по ключам и значениям. На выходе получаем кортеж 
#     print(items, end=' ')
    

# print('\n')   
# a, b, *c = (123, 456, 567, 678, 789) # Или должно быть одинаковое количество с права и слева, или же ставим зверзочку 
# print(a)                             # и лишнее распределяется на тот элемент. * ставится перед любым элементом
# print(b)
# print(c)

# print('\n')
# for key, value in my_dict.items():     # Проходим в циклн по ключам и значениям. На выходе получаем кортеж. Почти тоже самое, что и выше
#     print(key, value, sep=' -||- ', end=' ')
    
print('\n')    
print(*'Python', 'my', 'world', sep='-', end='\n') # sep - это разделитель между аргументами, по умолчанию ставится пробел.
print(*my_dict, sep='\n')                          # *- Это распаковка итерируемых элементов 

# 11:42
# my_dict = {"V": 23, "VX": 56, "VI": 90, "VI": 34, "VII": 123}

# print(my_dict)

# print(my_dict['V'])

# my_dict['V'] = 9999
# print(my_dict)

# my_dict['V'] += 1
# print(my_dict)

# my_dict['XXX'] = my_dict['V'] 
# del my_dict['V'] 
# print(my_dict)

# my_dict['VVV'] = my_dict.pop('VII') 
# print(my_dict)