# Two numbers are given as input to the program. 
# Write a program that determines whether the numbers have the same digits.

# Input Data Format:
# This program inputs two natural numbers, each on a separate line.

# Output format:
# It should print YES if the numbers have the same digits, and NO if they don't.

set1 = set(input())
set2 = set(input())
print('NO' if set1.isdisjoint(set2) else 'YES')