# Task 4

l1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
l2 = []

for el in l1:
    if l1.count(el) == 1:
        l2.append(el)
print(f'ОТВЕТ: {l2}')
