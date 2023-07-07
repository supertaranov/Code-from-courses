# Write a program that calculates the value ⌈x⌉ + ⌊x⌋ by a given real number x.

# Input data format:
# The input to the program is a single real number x.

# Output data format:
# The program should print a single number, the value of the expression.

#Note. ⌈x⌉ is the ceiling of the number, ⌊x⌋ - floor of the number.

from math import ceil, floor

x = float(input())
res = ceil(x) + floor(x)

print(res)