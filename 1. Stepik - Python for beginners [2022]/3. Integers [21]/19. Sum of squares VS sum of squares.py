# Write a program that reads two integers a and b 
# and displays the sum square and the sum of squares of those numbers.

# Input data format:
# This program inputs two integers, each on a separate line.

# Output format:
# The program should output the text according to the condition.

a = int(input())
b = int(input())
print('The square of the sum', a, 'and', b, 'equal to', (a+b)**2)
print('Sum of squares', a, 'and', b, 'equal to', a**2 + b**2)