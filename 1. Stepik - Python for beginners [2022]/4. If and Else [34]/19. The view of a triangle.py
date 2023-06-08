# Write a program that takes three positive numbers and determines the form of a triangle whose 
# side lengths are equal to the numbers entered.

# Input data format:
# The program takes three numbers as input - the lengths of the sides of an existing triangle.

# Output data format:
# The program should print the text - the type of triangle ('Equilateral', 'Isosceles' or 'Versatile').

a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('Equilateral')
elif a == b or a == c or b == c:
    print('Isosceles')
else:
    print('Versatile')