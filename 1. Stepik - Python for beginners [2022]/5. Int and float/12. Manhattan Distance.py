# Walking around Manhattan, you can't get from point A to point B by the shortest route. 
# Unless you know how to walk through walls, you're bound to walk along its parallel-perpendicular streets.
# Write a program that determines the Manhattan distance between two points whose coordinates are given.

# Input data format:
# The input to the program is four integers, each on a separate line - p1, p2, q1, q2.

# Output data format:
# The program should output a single number - the Manhattan distance.

x1, x2, y1, y2 = int(input()), int(input()), int(input()), int(input())
print(abs(x1-y1) + abs(x2-y2))