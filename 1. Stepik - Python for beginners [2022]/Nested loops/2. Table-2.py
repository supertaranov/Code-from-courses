# A natural number n (n≤ 9) is given. Write a program that prints a table of size n×5, 
# where in the i-th row contains the number i (numbers are separated by one space).

# Input data format:
# The program receives one natural number as input.

# Output data format:
# The program should output a table of size n×5 according to the condition.

# Note. There may be a space at the end of the line.

n = int(input())
for i in range(1, n+1):
    for j in range(5):
        print(i, end=' ')
    print()