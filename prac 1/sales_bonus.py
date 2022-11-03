"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

get sales
while sales >= 0
    calculate bonus
    get sales
do next thing
"""

sales = float(input("Enter sales: $"))
while sales > 0:
    if sales >= 1000:
        bonus_sales = sales * 0.15
        print(f"Your sales is ${sales} and including your bonus ${bonus_sales}")
        sales = float(input("Enter sales: $"))
    else:
        bonus_sales = sales * 0.10
        print(f"Your sales is ${sales} and including your bonus ${bonus_sales}")
        sales = float(input("Enter sales: $"))
print("BYE")


