import random


def test1():
    length = int(input("Length: "))
    width = random.randint(1,length)
    area = width * length
    print(f"Area of {length} x {width} is {area}")


# test1()


def print_grid(number_of_rows,number_of_columns):
    for r in range(number_of_rows):
        print("*"*number_of_columns)

# print_grid(3,7)


def main():
    height = random.uniform(1,2)
    weight = float(input("weight: "))
    if calculate_bmi(height,weight) < 15:
        print("Not considered overweight")
    else:
        print("overweight")


def calculate_bmi(height,weight):
    return weight / (height ** 2)


main()