# Write a program that determines the Euclidean distance between two points whose coordinates are given.

# Input data format:
# The input to the program is four real numbers, each on a separate line - x1, y1, x2, y2.

# Output data format:
# The program should output a single number - the Euclidean distance.

from math import *
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
p = ((x1 - x2)**2) + ((y1 - y2)**2)
print(sqrt(p))