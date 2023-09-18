# Given an odd natural number n. 
# Write a program that prints an isosceles star triangle with base equal to n according to the example:
# *
# **
# ***
# ****
# ***
# **
# *

# Input data format:
# The program receives one odd natural number as input.

# Output data format:
# The program should output a triangle according to the condition.

# Note. Use a nested for loop.

n = int(input())
for i in range(n//2+1):
    for j in range(i + 1):
        print('*', end='')
    print()
for i in range(n//2, 0, -1):
    for j in range(i):
        print('*', end='')
    print()