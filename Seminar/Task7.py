# Дано натуральное число. Требуется определить,является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

number=int(input("Введите натуральное число: "))
if number%4==0 and number%100!=0 or number%400==0:
    print("YES")
else:
    print("NO")    