# Write a program that calculates the value of a trigonometric expression for a given number of degrees x.

# Input data format:
# The program is inputted with a single real number x measured in degrees. 

# Output data format:
# The program should output a single number - the value of the trigonometric expression.

# Note. The math module contains a built-in function, radians(), which converts the angle from degrees to radians.

from math import *
x = float(input())
r = radians(x)
print(sin(r) + cos(r) + tan(r) * tan(r))