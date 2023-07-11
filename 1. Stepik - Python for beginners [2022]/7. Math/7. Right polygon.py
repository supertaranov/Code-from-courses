# A regular polygon is a convex polygon with all sides and all angles between adjacent sides equal.
# Two numbers are given: a natural number n and a real number a. 
# Write a program that finds the area of the specified regular polygon.

# Input data format:
# The program receives two numbers as input n and a, each on a separate line.

# Output data format:
# The program should output a real number - the area of the polygon.

from math import *
n = int(input())
a = float(input())
print((n * a**2 ) / (4 * tan(pi / n)))