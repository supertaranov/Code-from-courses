# The ordinal number of the month is given (1,2,..., 12). 
# Write a program that displays the number of days in that month. Assume that the year is a leap year.

# Note. Try to write the program so that it has no more than three conditions.

# Input Data Format:
# You enter a single integer number - the month number.

# Output data format:
# The program should output the number of days in that month.

m = int(input())
if m == 2:
    print('28')
elif m <= 7:
    print(30 + m%2 )
else: 
    print(31 - m%2 )