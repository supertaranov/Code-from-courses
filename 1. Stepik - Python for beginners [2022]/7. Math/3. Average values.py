# Input data format:
# The program inputs two real numbers a and b, each on a separate line.

# Output data format:
# The program should output 4 numbers - arithmetic mean, geometric mean, harmonic mean, and quadratic mean.

import math

a = float(input())
b = float(input())

arithmetic_mean = (a + b) / 2

geometric_mean = math.sqrt(a * b)

harmonic_mean = 2 / ((1 / a) + (1 / b))

quadratic_mean = math.sqrt((a ** 2 + b ** 2) / 2)

print(arithmetic_mean)
print(geometric_mean)
print(harmonic_mean)
print(quadratic_mean)