
# name = input("Enter your name: ")
# out_file = open(f"{name}.txt", "w")
# out_file.close()
#
#
# in_file = open(f"{name}.txt", "w")
# greeting = f"Hello {name}!"
# in_file.write(greeting)
# in_file.close()


with open("numbers.txt","r") as numbers_file:
    lines = numbers_file.readlines()

numbers = [int(line.strip()) for line in lines]
for number in numbers:
    print(number)

result = numbers[0] + numbers[1]
print(result)




numbers_file.close()



