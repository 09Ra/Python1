# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# Решение 1

# import random   # Импортируем библиотеку random

# max_watermelon=1
# min_watermelon=15
# num=random.randint(5,10) # Количество арбузов
# for i in range(num):
#     kg=random.randint(1,15)
#     print(kg)
#     if kg > max_watermelon:
#         max_watermelon = kg
#     elif kg < min_watermelon:
#         min_watermelon = kg

# print("Вес самого тяжелого арбуза равен: ", max_watermelon)  
# print("Вес самого легкого арбуза равен: ", min_watermelon)  


# Решение 2
import random   # Импортируем библиотеку random

kg=random.randint(1,15)    # Нашли вес первого арбуза рандомно и сразу его вес присваиваем на мин и мах
max_watermelon=kg
min_watermelon=kg
num=random.randint(5,10) # Количество арбузов
for i in range(num-1):   # Делаем -1, т.к первый вес первого арбуза определили ранее.
    kg=random.randint(1,15)
    print(kg)
    if kg > max_watermelon:
        max_watermelon = kg
    elif kg < min_watermelon:
        min_watermelon = kg

print("Вес самого тяжелого арбуза равен: ", max_watermelon)  
print("Вес самого легкого арбуза равен: ", min_watermelon)  


