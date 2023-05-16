# We call a number beautiful if it is a four-digit number divisible by 7 or by 17. 
# Write a program that determines whether the number you entered is beautiful or not. 
# The program should print "YES" if the number is beautiful, or "NO" otherwise.

# Input data format:
# A natural number is given as input to the program.

# Output data format:
# The program should output the text according to the problem condition.

num = int(input())
if 1000 <= num <= 9999 and (num % 7 == 0 or num % 17 == 0):
    print('YES')
else:
    print('NO')