"""
get score
    if score >= 0 and <=100
        if score => 90
            display excellent
        elif score => 50
            display pass
        else
        display bad
    else
    display invalid
"""
score = float(input("Enter score: "))
if 0 <= score <= 100:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("pass")
    else:
        print("bad")
else:
    print("invalid")

