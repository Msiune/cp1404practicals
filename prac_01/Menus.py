name = input("Name: ")
print("(H) - hello\n(G) - Goodbye\n(Q) - quit")
choice = input("Choice: ").lower()
while choice != 'q':
    if choice == 'h':
        print("hello")
    elif choice == 'g':
        print(f"Goodbye {name}")
    else:
        print("invalid")
    print("(H) - hello\n(G) - Goodbye\n(Q) - quit")
    choice = input("Choice: ").lower()
print("Finished")
