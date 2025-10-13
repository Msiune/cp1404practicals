"""Counting up by 2, starting on 1"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()
"""Counting up in 10"""
for n in range(0, 100, 10):
    print(n, end=' ')
print()
"""Decreasing from 20"""
for n in range(20, 0, -1):
    print(n, end=' ')
print()
print()
"""get user input of number of stars and print"""
number_of_star = int(input("Number of Stars: "))
print(number_of_star * "*")
print()

""" print lines of increasing stars """
bonus_star = number_of_star + 1
for n in range(1,bonus_star):
    print("*" * n)
print()