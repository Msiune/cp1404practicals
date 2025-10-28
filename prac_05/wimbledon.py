"""Wimbledon"""

# Read file
with open("wimbledon.csv", "r", encoding="utf-8-sig") as wimbledon_file:
    wimbledon_list = [line.strip().split(',') for line in wimbledon_file]

# the champions and how many times they have won
CHAMPION_TO_WIN = {}
wimbledon_champions = [champion[2] for champion in wimbledon_list]
for champion in wimbledon_champions:
    CHAMPION_TO_WIN[champion] = CHAMPION_TO_WIN.get(champion, 0) + 1

for champion, win in CHAMPION_TO_WIN.items():
    print(champion, win)

# print(CHAMPION_TO_WIN)

# the countries of the champions in alphabetical order
print("\n")
with open("wimbledon.csv", "r", encoding="utf-8-sig") as wimbledon_file:
    countries = [country[1] for country in wimbledon_list]

winning_countries = []

for country in countries:
    if country not in winning_countries:
        winning_countries.append(country)
    elif "Country" in winning_countries:
        winning_countries.remove("Country")
sorted_countries = sorted(winning_countries)
print(', '.join(sorted_countries))

