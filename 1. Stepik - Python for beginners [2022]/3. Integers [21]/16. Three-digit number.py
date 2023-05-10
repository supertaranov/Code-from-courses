# Write a program that calculates the sum and product of the digits of 
# a positive three-digit number.

# Input data format:
# The input to the program is a positive three-digit number.

# Output format:
# The program should output two numbers with explanatory text: sum of digits and product of digits.

num = int(input())
a = num // 100
b = (num // 10) % 10
c = num % 10
print("Sum of digits =", a + b + c)
print("Product of digits =", a * b * c)