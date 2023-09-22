# Given a natural number n. 
# Write a program that prints a numerical triangle according to the example:
# 1
# 22
# 333
# 4444
# 55555
# ...

# Input data format:
# The program receives one natural number as input.

# Output data format:
# The program should output a triangle according to the condition.

# Note. Use a nested for loop.

n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(i+1, end='')
    print()