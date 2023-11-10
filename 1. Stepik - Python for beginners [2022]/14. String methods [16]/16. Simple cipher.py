# A string of text is given to the program as input. 
# Write a program that translates each of its characters into the corresponding code from the Unicode character table.

# Input data format:
# The input to the program is a string of text.

# Output data format:
# The program should output the code values of the characters of the string separated by one space character.

s = input()
for i in range(len(s)):
    print(ord(s[i]), end=' ')