# An anagram is a word (phrase) formed by rearranging the letters that make up another word (or phrase). 
# For example, the English words evil and live are anagrams.

# This program has two words as input. Write a program that determines if they are anagrams.

# Input format:
# This program inputs two words, each on a separate line.

# Output format:
# The program should print YES if the words are anagrams and NO otherwise.

dict1, dict2 = {}, {}
for i in input():
    dict1[i] = dict1.get(i, 0) + 1
for i in input():
    dict2[i] = dict2.get(i, 0) + 1
print('YES' if dict1 == dict2 else 'NO')