# A natural number is received for processing. 
# You need to write a program that displays the product of digits of the entered number on the screen. 
# The programmer was in a hurry and wrote the program incorrectly.

# Find all the errors in this program (there are exactly 3). 
# It is known that each error affects only one line and can be corrected without changing other lines.

n = int(input()) #1
product = 1 #2
while n > 0: #3
    digit = n % 10
    product = product * digit
    n //= 10
print(product)