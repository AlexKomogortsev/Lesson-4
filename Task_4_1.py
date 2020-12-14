# Task 1

from sys import argv


def zarplata(hours, rate, bonus):
    return hours * rate + bonus


_, hours, rate, bonus = argv
print(zarplata(int(hours), int(rate), int(bonus)))
