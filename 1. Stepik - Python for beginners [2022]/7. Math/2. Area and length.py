# Write a program that determines the area of a circle and the length of a circle with a given radius R.

# Input data format:
# The program is inputted with a single real number R.

# Output data format:
# The program should output two numbers - the area of the circle and the length of the circle of radius R.

from math import *
r = float(input())
print(pi * r**2)
print(2 * pi * r)