"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
The ValueError in line 15 will occur when numerator or denominator is not a valid int(input)
2. When will a ZeroDivisionError occur?
ZeroDivisionError in line 18 will occur when denominator int(input) = 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
def exception_demo_1():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")

# exception_demo_1()

# Different variation without ZeroDivisionError 
def exception_demo_2():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator != 0:
            fraction = numerator / denominator
            print(fraction)
        else:
            print("Cannot be divided by zero!")
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    print("Finished.")

exception_demo_2()