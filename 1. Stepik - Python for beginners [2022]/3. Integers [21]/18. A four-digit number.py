# Write a program to find the digits of a four-digit number.

# Input data format:
# The input to the program is a positive four-digit integer.

# Output data format:
# The program should output the text according to the problem's condition.

num = int(input())
d = (num % 10 )
c = (num % 100) // 10
b = (num % 1000) // 100
a = num // 1000
print("The number in the thousands position is equal to", a)
print("The number in the position of hundreds is equal", b)
print("The number in the position of tens is equal", c)
print("The number in the position of ones is equal", d)