# Write a program that determines whether the year with the given number ends with two zeros. 
# If the year ends, print "YES", otherwise print "NO".

# Input data format:
# The input for the program is a natural number.

# Output format:
# The program should output the text according to the problem's condition.

num = int(input())
if num % 100 == 0:
    print('YES')
else:
    print('NO')