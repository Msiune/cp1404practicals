def a():
    for i in range(0,110,10):
        print(i, end=' ')
    print()


def b():
    for i in range(20,0,-1):
        print(i, end=' ')
    print()


def c():
    number = input("Number of Stars:")
    for stars in range(int(number)):
        print(end='*')
    print()


def d():
    number = int(input("Number of Stars:"))
    for stars in range(1,number+1):
        print("*"*stars)

# a()
# b()
# c()
# d()
