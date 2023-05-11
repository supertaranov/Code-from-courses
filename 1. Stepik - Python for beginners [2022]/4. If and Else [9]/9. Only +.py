# Write a program that reads three numbers and counts the sum of positive numbers only.

# Input data format:
# The program is inputted with three integers.

# Output data format:
# The program should print one number, the sum of the positive integers.

# Note. If there are no positive numbers then output 0.

num1, num2, num3 = int(input()), int(input()), int(input())
sum = 0
if num1 < 0:
    num1 = 0
if num2 < 0:
    num2 = 0
if num3 < 0:
    num3 = 0
print(num1+num2+num3)