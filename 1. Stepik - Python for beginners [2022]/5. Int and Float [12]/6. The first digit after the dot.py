# A positive real number is given. Print its first digit after the decimal point.

# Input data format:
# A positive real number is given as input to the program.

# Output data format:
# The program should print the number in accordance with the problem.

num = float(input())
x = num * 10
c = x % 10
print(int(c))