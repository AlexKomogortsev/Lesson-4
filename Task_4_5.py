# Task 5

from functools import reduce


def multiply(a, b):
    return a * b


l = [el for el in range(100, 1001) if el % 2 == 0]

print(f'ОТВЕТ: {reduce(multiply, l)}')