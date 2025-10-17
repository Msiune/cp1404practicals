"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
ABBREVIATION_TO_STATES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                          "WA": "Western Australia",
                          "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania",
                          "SA": "South Australia"}
# print(ABBREVIATION_TO_STATES)
#
# state_code = input("Enter short state: ").upper()
# while state_code != "":
#     if state_code in ABBREVIATION_TO_STATES:
#         print(state_code, "is", ABBREVIATION_TO_STATES[state_code])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()



abbreviation = list(ABBREVIATION_TO_STATES.keys())
state_name = list(ABBREVIATION_TO_STATES.values())
for i in range(len(ABBREVIATION_TO_STATES)):
    print(f"{abbreviation[i]:3} is {state_name[i]}")


print(ABBREVIATION_TO_STATES)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", ABBREVIATION_TO_STATES[state_code])
        state_code = input("Enter short state: ").upper()
    except KeyError:
        print("Invalid short state")
        state_code = input("Enter short state: ").upper()

