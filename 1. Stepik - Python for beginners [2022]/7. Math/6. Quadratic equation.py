# There are three real numbers a, b, c. Write a program that finds real roots of a quadratic equation.

# Input data format:
# The program inputs three real numbers a ≠ 0,b,c, each on a separate line.

# Output data format:
# The program should print the real roots of the equation if they exist or the text "No Roots" otherwise.

# Note. If the equation has two roots then output them in ascending order.

from math import *

a = float(input())
b = float(input())
c = float(input())
d = b**2-4*a*c

if d < 0:
    print('No Roots')
elif d == 0:
    print(-b / (2*a))
elif d > 0:
    x1 = (-b - d ** 0.5) / (2*a)
    x2 = (-b + d ** 0.5) / (2*a)
    print(min(x1, x2))
    print(max(x1, x2))