# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло 
# ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint

n=[randint(0,10) for i in range(randint(3,20))]
print(n)
print(f"Всего кустов черники на грядке {len(n)}")
count=0
max_berries=0
count_berries=0
while count<len(n):
    count_berries=n[count-2]+n[count-1]+n[count]
    
    if count_berries>max_berries:
        max_berries=count_berries
        count+=1
    else:
        count+=1
    print(count_berries)    
print(f"Максимального числа ягод, которое может собрать за один заход собирающий модуль равен {max_berries}")        
            