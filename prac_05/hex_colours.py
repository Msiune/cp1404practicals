"""start time 12:00 --> End time 5:34"""

COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                  "Alizarin crimson": "#0048ba", "Amaranth": "#e52b50", "Amber": "#ffbf00",
                  "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                  "AntiqueWhite2": "#eedfcc"}
# list of colours
colours = list(COLOUR_TO_CODE.keys())
# list of codes
codes = list(COLOUR_TO_CODE.values())
# display ten colours (names)
print("list of colours")
for i in range(len(colours)):
    print(colours[i], end=", ")

"""list of all the COLOUR_TO_CODE in uppercase"""
colours_in_uppercase = [colour.upper() for colour in colours]

print("\n")
colour = input("Enter colour: ").upper()
# while loop that ends on an empty string
while colour != "":
    if colour in colours_in_uppercase:
        # colour_index variable is used for finding the location of colours and codes
        colour_index = colours_in_uppercase.index(colour)
        print(f"The code for the colour {colours[colour_index]} is: {codes[colour_index]}")
        colour = input("Enter colour: ").upper()
    else:
        print("Invalid colour")
        colour = input("Enter colour: ").upper()