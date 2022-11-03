"""
get name
display menu
get choice
while choice != q
    if choice == h
        display hello name
    else if choice == g
        display goodbye name
    else if choice == q
        do n-th task
    else
        display invalid input error message
    display menu
    get choice
display finished
"""
name = input("name  :")
MENU = print("(H)ello \\ (G)oodbye \\ (Q)uit")
choice = input("Choice  :")
while choice != 'q':
    if choice == 'h':
        print(f"hello {name}")
        choice = input("Choice  :")
    elif choice == 'g':
        print(f"goodbye {name}")
        choice = input("Choice  :")
    else:
        print(f"incorrect {name}")
        choice = input("Choice  :")
print("Finished")
