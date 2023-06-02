# Two sentences are given as input to the program. 
# Write a program that determines whether they are anagrams or not. 
# Your program should ignore case, punctuation, and spaces.

# Input format:
# The program inputs two sentences, each on a separate line.

# Output format:
# It should print YES if the sentences are anagrams, and NO otherwise.

# Note. The text may contain spaces and punctuation marks besides words. 
# There are no other characters in the text.

def s(word):
    result = {}
    # form a dictionary where the keys are each character of the string
    for i in word.lower():
        result[i] = result.get(i, 0) + 1
    keys = ['.', ',', ';', ':', '-',' ', '!', '?']
    # remove these characters as keys from the dictionary
    for key in keys:
        result.pop(key, None)
    return result

print('YES' if s(input()) == s(input()) else 'NO')