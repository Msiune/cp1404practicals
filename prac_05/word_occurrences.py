"""
word_occurrences
estimate: 1hour
actual: 50min
"""

text = input("Enter text: ")
WORDS_AND_COUNT = {}
for word in text.split():
    WORDS_AND_COUNT[word] = WORDS_AND_COUNT.get(word, 0) + 1

longest_word = ""

words = list(WORDS_AND_COUNT.keys())
count = list(WORDS_AND_COUNT.values())
for i in range(len(WORDS_AND_COUNT)):
    if len(words[i]) > len(longest_word):
        longest_word = words[i]
    print(f"{words[i]:{len(longest_word)}} is {count[i]}")
