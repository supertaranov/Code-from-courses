# The input to the program is two lines of text containing numbers. 
# Write a program that determines the number of numbers that are in both the first line and the second.

# Input Data Format:
# This program inputs two lines of text containing numbers separated by a space character.

# Output data format:
# The program should output the number of numbers that are contained in both the first 
# and second lines at the same time.

set1 = set(input().split())
set2 = set(input().split())
print(len(set1 & set2))