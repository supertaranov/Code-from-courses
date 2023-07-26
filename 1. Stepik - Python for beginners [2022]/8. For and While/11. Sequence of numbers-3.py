# Two integers are given m and n (m>n). 
# Write a program that outputs all odd numbers from m to n inclusive in descending order.

# Input data format:
# Two integers m and n, each on a separate line.

# Output data format:
# The program should output numbers according to the problem condition.

m, n = int(input()), int(input())
for i in range(m, n-1, -1):
    if i % 2 != 0:
        print(i)