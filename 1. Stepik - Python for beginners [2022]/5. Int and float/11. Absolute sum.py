# Five numbers are given a1, a2, a3, a4, a5.
# Write a program that calculates the sum of their modules.

# Input data format:
# The input to the program is five real numbers a1, a2, a3, a4, a5, each on a separate line.

# Output data format:
# The program should output a single number - the sum of the moduli of the entered numbers.

a, b, c, d, e = float(input()), float(input()), float(input()), float(input()), float(input())
print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))