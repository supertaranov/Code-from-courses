# Two integers a and b (a≤b) are given as input to the program. 
# Write a program that counts the number of numbers in the range from a to b inclusive, the cube of which ends in 4 or 9.

# Input data format:
# The program receives two integers a and b (a≤b).

# Output data format:
# The program should output one integer number according to the program condition.

# Note. The cube of the number a is its third degree 3.

a, b = int(input()), int(input())

cnt = 0
for i in range(a, b + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        cnt += 1

print(cnt)