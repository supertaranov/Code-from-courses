# Two integers m and n are given. 
# Write a program that outputs all numbers from m to n inclusive in ascending order if m < n, 
# or in descending order otherwise.

# Input data format
# The input to the program is two integers m and n, each on a separate line.

# Output data format
# The program should output numbers according to the problem condition.

n, m = int(input()), int(input())

if n < m:
    for i in range(n, m + 1):
        print(i)
else:
    for i in range(n, m - 1, -1):
        print(i)