#Требуется найти N-е число Фибоначчи
 
def find_fib(n):
    if n in [1,2]:
        return 1
    return find_fib(n-1)+find_fib(n-2)

n = int(input("Введите номер числа Фибоначчи N: "))
print(find_fib(n))
 