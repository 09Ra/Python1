# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.


# Решение №1 домашка для программистов

# import random

# num = random.randint(2,20)

# count1=0
# count2=0

# for i in range(num):
#     coin = random.randint(0,1)
#     print(coin)
#     if coin==0:
#         count1+=1
#     else:
#         count2+=1 
# print("На столе лежат",num, "монет")        
# print("Из них", count1, "лежат вверх решкой") 
# print("Из них", count2, "лежат вверх гербом")       
# if count1>count2:
#     print("Минимальное количество монет, которые нужно перевернуть", count2)   
# else:
#     print("Минимальное количество монет, которые нужно перевернуть", count1)           
    


# Решение №2 домашка для аналитиков

coins = [0, 1, 0, 1, 1, 0]

count1=0
count2=0

for i in range(len(coins)):
    if coins[i]==0:
        count1+=1
    else:
        count2+=1 
        

      
if count1>count2:
    print(count2)   
else:
    print(count1)