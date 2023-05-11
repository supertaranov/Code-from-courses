# Write a program that determines whether a number is even or odd.

# Input data format:
# The input to the program is a single integer.

# Output format:
# The program should output "Even" if the number is even, and "Odd" if the number is odd.

a = int(input())
if a % 2 == 0:
    print('Even')
else:
    print('Odd')