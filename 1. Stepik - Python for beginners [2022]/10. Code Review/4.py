# A natural number is received for processing. 
# You need to write a program that displays the maximum digit of the number divisible by 3. 
# If there are no digits divisible by 3 in the number, it is required to display "NO". 
# The programmer was in a hurry and wrote the program incorrectly.

# Find all the errors in this program (there are exactly 5 of them). 
# It is known that each error affects only one line and can be corrected without changing other lines.

# Note 1. The number 0 is divisible by any natural number.
# Note 2. You can add the necessary lines of code if necessary.

n = int(input())
max_digit = -1 #wrong
while n > 0:
    digit = n % 10
    if digit % 3 == 0: 
        if digit > max_digit: #wrong
            max_digit = digit #wrong
    n = n // 10 #wrong
if max_digit == -1: #wrong
    print('NO')
else:
    print(max_digit)