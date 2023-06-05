# You are given a dictionary consisting of pairs of synonyms. 
# There are no repetitive words in the dictionary. 
# Write a program that finds a synonym for one given word.

# Input data format:
# The program inputs the number of pairs of synonyms n. It is followed by n lines, 
# each line contains two synonym words. This is followed by one word whose synonym must be found.

# Output data format:
# The program should print one word that is a synonym of the one you typed.

# Note 1. It is guaranteed that the synonym of the word exists in the dictionary.
# Note 2. All words in the dictionary start with a capital letter.

n = int(input())
text = [input().split() for _ in range(n)] 
word = input()
dict1 = dict(text)

for key, value in dict1.items():
    if value == word:
        print(key)
    elif key == word:
        print(value)