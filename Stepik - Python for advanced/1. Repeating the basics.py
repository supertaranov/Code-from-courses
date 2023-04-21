# Task 1
# The program is given two integers A and B as input. 
# Write a program that outputs:
# 1. the sum of the numbers
# 2. the difference between the numbers
# 3. the product of the numbers
# 4. quotient of the numbers
# 5. the integer part of dividing the number
# 6. the remainder of dividing the number
# 7. the square root of the sum of their 10 degrees

a, b = int(input()), int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print((a**10 + b**10) **0.5)