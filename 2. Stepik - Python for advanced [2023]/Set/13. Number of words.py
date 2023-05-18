# Write a program to determine the total number of different words in a line of text.

# Input data format:
# The program takes a string of text as input.

# Output data format:
# The program has to output a single number - the total number of different words in the string, 
# not case-sensitive.

# Note 1. A word is a sequence of non-white characters, words separated by one or more spaces.
# Note 2. The punctuation marks .,;:-?! are neglected.

words = [word.lower().strip('.,;:-?!') for word in input().split()]

print(len(set(words)))