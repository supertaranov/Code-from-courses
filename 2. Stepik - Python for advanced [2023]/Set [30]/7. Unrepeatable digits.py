# A string consisting of digits is given as input to the program. 
# Is it true that none of the digits in the string is repeated?

# Input data format:
# The program input is a string consisting of digits

# Output format:
# The program should print YES if none of the digits in the string is repeated, and NO otherwise.

n = input()
print('YES' if len(n) == len(set(n)) else 'NO')