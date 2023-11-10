# A natural number is received for processing. 
# You need to write a program that displays the first (highest) digit of the number on the screen. 
# The programmer was in a hurry and wrote the program incorrectly.

# Find all the errors in this program (there are exactly 2). 
# It is known that each error affects only one line and can be corrected without changing other lines.

n = int(input())
while n > 9:
    n //= 10
print(n)