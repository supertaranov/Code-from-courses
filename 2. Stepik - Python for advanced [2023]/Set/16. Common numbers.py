# This program is inputted with two lines of text containing numbers. 
# Write a program that outputs all the numbers in ascending order that are in both the first and second lines.

# Input data format:
# The input to the program is two lines of text containing numbers separated by a space character.

# Output format:
# The program should print the set of numbers occurring in both lines.

mylist1 = [int(i) for i in input().split()]
myset1 = set(int(i) for i in input().split())
print(*sorted(myset1.intersection(mylist1)))