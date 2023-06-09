# Write a program that reads the lengths of the two cathetuses in a right triangle and prints its area.

# Input data format:
# The program inputs two floating point numbers - the lengths of the cathetuses, each on a separate line.

# Output format:
# The program should output one number - the area of the triangle.

x, y = float(input()), float(input())
print(1/2 * x * y)