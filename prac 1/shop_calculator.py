"""
get number of items
    for number of items
        display random price
        add price together
    display total price
"""
import random
shopping_cart = 0
number_of_items = int(input("Number of items    :"))
# print(number_of_items)
for items in range(number_of_items):
    random_items = float(random.uniform(1,100))
    # print(random_items)
    print(f"price of item ${random_items:.2f}")
    shopping_cart = random_items + shopping_cart
print(f"Total price of all {number_of_items} items is ${shopping_cart:.2f}")