# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# Решение №1

# def prime_number(number):
#     for i in range(2,number-1):
#         if number%i==0:
#             return "no"
#     return "yes"
    
# n=int(input("Введите число: "))  
# print(prime_number(n))  


# Решение №2

def prime_number(number):
    if number == 2:
        return True
    elif number % 2 == 0:
        return False
    for i in range(3,int((number**0.5)+1),2): # Сокращаем количество итеррации засчет того, что берем шаг 2
        if number%i==0:
            return False
    return True
    
n=int(input("Введите число: "))  
if (prime_number(n)):
    print("yes") 
else:
    print("no")    