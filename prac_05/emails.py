"""
word_occurrences
estimate: 1hour
actual: 50min
"""
EMAIL_TO_NAME = {}


def main():
    email = input("Email: ")
    while email != "":
        if "@" in email:
            location = email.find("@")
            full_name = email[0:location]
            # this function is used to confirm your first name
            full_name = name_confirmation(full_name)
            EMAIL_TO_NAME[email] = full_name
            email = input("Email: ")
        else:
            print("invalid email")
            email = input("Email: ")
    print("\n")
    emails = list(EMAIL_TO_NAME.keys())
    names = list(EMAIL_TO_NAME.values())
    for i in range(len(EMAIL_TO_NAME)):
        print(f"{names[i]:3} ({emails[i]})")


def name_confirmation(full_name):
    confirmation = input(f"is your name {full_name} (Y/N)")
    if confirmation == "Y":
        return full_name
    else:
        full_name = input("Enter your name: ")
        while full_name == "":
            full_name = input("Enter your name: ")
        return full_name

main()
