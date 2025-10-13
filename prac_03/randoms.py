import random
# print(random.randint(5, 20))  # line 1
# print(random.randrange(3, 10, 2))  # line 2
# print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# Line 1 displayed "19"
# What was the smallest number you could have seen, what was the largest?
# Smallest number: 5 largest number: 20


# What did you see on line 2?
# Line 1 displayed "5"
# What was the smallest number you could have seen, what was the largest?
# Smallest number: 3 largest number: 10
# Could line 2 have produced a 4?
# Line 2 cannot produce 4 because the range starts at 3 and counts up in the increment of 2


# What did you see on line 3?
# Line 1 displayed "3.9691938877432054"
# What was the smallest number you could have seen, what was the largest?
# Smallest number: 2.5 largest number: 5.5


# Write code, not a comment, to produce a random number between 1 and 100 inclusive.

print(random.randint(1, 100))