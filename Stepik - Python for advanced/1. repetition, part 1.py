# Task 1
# The program is given two integers A and B as input. 
# Write a program that outputs:
# the sum of the numbers
# the difference between the numbers
# the product of the numbers
# quotient of the numbers
# the integer part of dividing the number
# the remainder of dividing the number
# the square root of the sum of their 10 degrees

a, b = int(input()), int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print((a**10 + b**10) **0.5)

# Task 2
# Write a program to calculate and estimate the human body mass index. 
# The index shows whether a person weighs more 
# or less than the norm for their height. 
# Weight is measured in kilograms, and height is measured in meters. 
# The mass of a person is considered optimal if 
# his index is between 18.5 and 25. If the index is less than 18.5, 
# then it is considered that a person weighs below the norm. 
# If the index value is greater than 25, then it is assumed that the person weighs more than normal.
# The program should output "Optimal mass" if the index is between 18.5 and 25 (inclusive). 
# "Insufficient mass" if the index is less 18.5
# "Overweight" if the index value is greater 25.

def index(weight, height):
    result = weight / (height * height)
    return result

weight, height = float(input()), float(input())

if 18.5 <= index(weight, height) <= 25:
    print("Optimal mass")
elif index(weight, height) < 18.5:
    print("Insufficient mass")
else:
    print("Overweight")