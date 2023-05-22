# This program inputs two lines of text containing numbers. 
# Write a program that outputs all the numbers in ascending order that are in the first line but not in the second.

# Input data format:
# This program inputs two lines of text that contain numbers separated by a space character.

# Output format:
# The program has to print the set of numbers that occur in the first line only.

set1  = set(int(i) for i in input().split())
set2  = set(int(i) for i in input().split())
print(*sorted(set1.difference(set2)))