# Two integers m and n ( m≤n) are given. Write a program that outputs all numbers from m to n inclusive.

# Input data format:
# The program is given two integers m and n, each on a separate line.

# Output data format:
# The program should output numbers according to the problem condition.

m = int(input())
n = int(input())

for i in range(m, n + 1):
    print(i)