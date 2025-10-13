numbers = [3,1,4,1,5,9,2]
numbers[0] = "ten"
print(numbers[0])
numbers[-1] = 1
print(numbers[-1])

numbers_starting_from_three = numbers[2:7:]
print(numbers_starting_from_three)

def is_element():
    if 9 in numbers:
        print("Element is present")
    else:
        print("Element is not present")

is_element()