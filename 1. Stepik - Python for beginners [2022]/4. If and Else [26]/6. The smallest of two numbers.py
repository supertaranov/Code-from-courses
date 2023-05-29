# Write a program that determines the smallest of two numbers.

# Input data format:
# The input to the program is two different integers.

# Output data format:
# The program should output the smallest of the two numbers.

num1, num2 = int(input()), int(input())
if num1 < num2:
    print(num1)
else:
    print(num2)