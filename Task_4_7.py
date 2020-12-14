# Task 7


def fact(n):
    a = 1
    for el in range(1, n + 1):
        a = a * el
        yield a


n = int(input('Введите целое положительное число: '))

for el in fact(n):
    print(el)
