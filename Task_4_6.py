# Task 6_1

from time import sleep
from itertools import count, cycle
#
# for x in count(10):
#     print(x)
#     sleep(0.3)
#     if x == 35:
#         break

# Task 6_2

cnt = 0
l = [3, 2, 1, 5, 8]
for x in cycle(l):
    print(x)
    sleep(0.5)
    cnt += 1
    if cnt == 15:
        break