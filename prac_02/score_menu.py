def main():
    MENU = "(G)et a valid Score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != 'Q':
        if choice == "G":
            score = int(input("Score: "))
            score = is_score_valid(score)
            print(f"score: {score} Congratulation this is a valid score")
        elif choice == "P":
            score = int(input("Score: "))
            score = is_score_valid(score)
            result = display_result(score)
            print(f"your score: {score}, result: {result}")
        elif choice == "S":
            score = int(input("Score: "))
            score = is_score_valid(score)
            star = print_stars(score)
            print(f"your score: {score}\nstars: {star}")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Choice: ").upper()


def is_score_valid(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def display_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    return score * "*"


main()
