# Given a natural number n. 
# Write a program that prints a numerical triangle with height equal to n, according to the example:

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# ...

# Input data format:
# The input to the program is one natural number.

# Output data format:
# The program should output a triangle according to the condition.

# Note. Use a nested for loop.

counter = 0
n = int(input())
for i in range(n):
    for j in range(i + 1):
        counter += 1
        print(counter, end=' ')
    print()