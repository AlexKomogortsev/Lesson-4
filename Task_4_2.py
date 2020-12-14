# Task 2

l1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
l2 = []

l2 = [el for index, el in enumerate(l1) if index > 0 and l1[index] > l1[index - 1]]
print(l2)
