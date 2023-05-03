# The program is fed two natural numbers n and m, 
# each on a separate line — the number of rows and columns in the matrix. 
# Next, the matrix elements themselves are introduced — words, each on a separate line; 
# elements of the first line, then the second, and so on, go in a row.

# Write a program that reads the matrix elements one by one, 
# outputs them as a matrix, outputs an empty row, and again the same matrix, 
# but already swapping rows with columns: the first row is output as the first column, and so on.

# Input data format:
# The program is fed two numbers n and m is the number of rows and columns in the matrix, 
# followed by n × m words, each on a separate line.

# Output data format:
# The program should output the read matrix, followed by an empty row, 
# and the same matrix, but swapping rows with columns. Separate matrix elements with a single space.

n, m = int(input()), int(input())  

matrix = [[0] * m for _ in range(n)]    

for i in range(n):                     
    for j in range(m):   
        matrix[i][j] = input()

for a in matrix:                     
        print(*a, end='\n')

print()

for j in range(m):                     
    for i in range(n):   
        print(matrix[i][j], end=' ')
    print()