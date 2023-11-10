# The input to the program is a string of text consisting of words separated by exactly one space. 
# Write a program that counts the number of words in it.

# Input data format: 
# A string of text is given to the program as input.

# Output data format:
# The program should output the number of words.

# Note 1. The text string does not contain spaces at the beginning and end.
# Note 2. Use the count method to solve the problem.

s = input()
x = s.count(' ') + 1
print(x)