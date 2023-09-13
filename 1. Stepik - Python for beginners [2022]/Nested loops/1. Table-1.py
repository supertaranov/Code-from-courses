# A natural number n (n≤ 9) is given. 
# Write a program that prints a table of size n×3 consisting of this number (numbers are separated by one space).

# Input data format:
# The program receives one natural number as input.

# Output data format:
# The program should print a table of size n×3 consisting of the given number.

# Note. There may be a space at the end of the line.

n = int(input())
for i in range(n):
    print(n, n, n)