# Given a natural number n (n ≤ 9). 
# Write a program that prints the addition table for all numbers from 1 to n (inclusive) according to the example.

# Input data format:
# The input to the program is one natural number.

# Output format:
# The program should print the addition table for all numbers from 1 to n.

# Note 1: We mean the addition table from 1 to 9 (inclusive).
# Note 2. There may be a space at the end of the line.

n = int(input())
for i in range(1, n+1):
    for j in range(1, 10):
        print(i, '+', j, "=", i+j)
    print()