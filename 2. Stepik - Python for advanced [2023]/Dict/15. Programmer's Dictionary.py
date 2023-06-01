# Programmers, as you already know, are constantly learning and use a very specific language 
# to communicate with each other. To systematize your growing professional lexicon, we created this task. 
# Write a program to create a little dictionary of slang expressions, and then on request it 
# will return the values from the dictionary.

# The format of the input data:
# The first line contains an integer n - the number of words in the dictionary. 
# The next n lines contain words and their definitions, separated by a colon and a space character. 
# The next line contains an integer m - the number of search words whose definition you want to output. 
# The next m lines contain the words themselves, one per line.

# Output data format:
# For each word, regardless of character case, if it is present in the dictionary you must print its definition. 
# If the word is not in the dictionary, the program should print "Not found", without the quotes.

# Note 1. You can take a look at the mini-dictionary for beginners here.
# Note 2. It is guaranteed that the defined word or phrase does not contain a colon (:) followed by a space.

dict1 = {}
n = int(input())
for _ in range(n):
    key, value = input().split(': ')
    dict1[key.lower()] = value

m = int(input())
for _ in range(m):
    print(dict1.get(input().lower(), 'Not found'))