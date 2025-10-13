"""Quick Pick Lottery Ticket Generator"""

import random

NUMBER_OF_COUNTS = 6
MAX = 45
MIN = 1


amount_of_picks = int(input("How many quick picks? "))
list_of_picks = []
while amount_of_picks > len(list_of_picks):
    pick = []
    while len(pick) < NUMBER_OF_COUNTS:
        random_number = random.randint(MIN, MAX)
        if random_number not in pick:
            pick.append(random_number)
    list_of_picks.append(pick)
# print(list_of_picks)

for i in list_of_picks:
    layout = (" ".join(f"{i:>2}" for i in i))
    print(f"{layout}")
