from random import randint
max1=20000
min1=20000
all=int(input("Введите количество сравниваемых арбузов:  "))
number=1
while all>=number:
    arbuz=int(randint(10000,30000))
    print(arbuz, end=', ' )
    if arbuz>max1:
        max1=arbuz
        number=number+1
    elif arbuz<min1:
        min1=arbuz
        number=number+1
    else:
        number=number+1
print("Самый тяжелый арбуз весит: ",max1)  
print("Самый легкий арбуз весит: ", min1)          
         
    