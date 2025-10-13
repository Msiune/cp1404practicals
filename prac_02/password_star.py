
def main():
    password = input("Password: ")
    while len(password) < 8:
        print("Password must be at least 8 characters long")
        password = input("Password: ")
    print(f"Your password is: {(len(password)) * "*"}\n{password}")

main()