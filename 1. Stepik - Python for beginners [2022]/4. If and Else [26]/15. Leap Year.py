# Write a program that determines whether the year with the given number is a leap year. 
# If the year is leap year, print "YES", otherwise print "NO".

# A year is leap year if its number is a multiple of 4, but not a multiple of 100, 
# or if it is a multiple of 400.

# The input format:
# The input for the program is a natural number.

# Output data format:
# The program should print the text according to the problem.

year = int(input())
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('YES')
else:
    print('NO')