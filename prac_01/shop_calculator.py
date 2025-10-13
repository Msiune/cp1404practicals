"""The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen."""

number_of_items = int(input("Number of items: "))
total_shopping = 0
for i in range(number_of_items):
    price = int(input("price of item: "))
    total_shopping = price + total_shopping
print(f"Total price for {number_of_items} items is ${total_shopping}")

