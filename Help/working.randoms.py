# Есть три срособа импортировать модуль random
# 1. import random  -  Импортируем модуль рандом
# 2. from random import randint - импортирует функцию(метод) randint из модуля random
# 3. from random import *  - импортирует все функции модуля random. Такой способ является энергозатратным





# Способ №1

# import random  # Импортируем модуль рандом

# rnd=random.randint(5,10) # рандомно задаем количество элементов в массиве

# list_1=[random.randint(-20,20) for i in range(rnd)] # рандомно заполняем список элементами
# print(list_1)



# Способ №2

from random import randint

list_1=[randint(-20,20) for i in range(1,10)]
print(list_1)


# Способ №3 Кирилл Панфилов

from random import randint
 
print(list_1 := [randint(-5,5) for _ in range(1,10)]) # _ заменяет i

