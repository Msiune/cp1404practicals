"""
CP1404/CP5632 - Practical
Program to determine score status
"""

# score = float(input("Enter score: "))
# if score < 0 or score > 100:
#     print("Invalid score")
# elif score >= 90:
#     print("Excellent")
# elif score >= 50:
#     print("Passable")
# else:
#     print("Bad")

import random

def main():
    score = float(input("Enter score: "))
    valid = is_score_valid(score)
    if valid is True:
        print("Your score is invalid.")
    else:
        random_grade = random_score()
        grade = determine_score(score,random_grade)
        print(f"Score: {grade[0]}, Random Score({random_grade}): {grade[1]}")

def is_score_valid(score):
    return score < 0 or score > 100

def determine_score(score,random_grade):
    if score >= 90:
        score =  "Excellent"
    elif score >= 50:
        score = "Passable"
    else:
        score = "Bad"

    if random_grade >= 90:
        random_grade = "Excellent"
    elif random_grade >= 50:
        random_grade = "Passable"
    else:
        random_grade = "Bad"

    return score,random_grade


def random_score():
    random_number = random.randint(1, 100)
    return random_number

main()