# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения списка или список задан изначально.


import random


list_1=[random.randint(1,20) for i in range(10)]
print(list_1)
coint=0
for j in range(len(list_1)-1):
    if list_1[j+1]>list_1[j]:
        coint+=1
print(coint)        
        