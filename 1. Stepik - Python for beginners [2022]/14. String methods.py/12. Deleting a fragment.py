# The input to the program is a string of text in which the letter "h" occurs at least twice. 
# Write a program that removes the first and the last occurrence of the letter "h" from this string, 
# as well as all characters between them.

# Input data format:
# The input to the program is a string of text.

# Output data format:
# The program should output the text according to the problem condition.

s = input()
a = s.find('h')
b = s.rfind('h')
print(s[:a] + s[b+1:])