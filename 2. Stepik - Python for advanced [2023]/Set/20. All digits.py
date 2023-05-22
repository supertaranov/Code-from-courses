# Two numbers are given as input to the program. 
# Write a program that determines whether the record of the first number includes 
# all the digits contained in the record of the second number (regardless of the repetition, 
# that is, the number of digits) or not.

# Input data format:
# The program inputs two natural numbers, each on a separate line.

# Output format:
# It should print YES if the first number contains all digits of the second number and NO otherwise.

set1 = set(input())
set2 = set(input())
print('YES' if set1.issuperset(set2) else 'NO')