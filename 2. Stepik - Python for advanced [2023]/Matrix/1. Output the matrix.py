# The program is fed two natural numbers n and m, 
# each on a separate line — the number of rows and columns in the matrix. 
# Next, the matrix elements themselves are introduced — words, 
# each on a separate line; elements first of the first line, 
# then the second, and so on, go in a row.

# Write a program that first reads the matrix elements one by one, then outputs them as a matrix.

# Input data format:
# Two numbers n and m are given to the program as input — 
# the number of rows and columns in the matrix, followed by n × m words, each on a separate line.

# Output data format:
# The program should output the read matrix, separating its elements with a single space.

n, m = int(input()), int(input())  

matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):   
        matrix[i][j] = input()

for k in matrix:
        print(*k, end='\n')