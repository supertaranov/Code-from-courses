# Write a program that takes three positive numbers and determines if there is 
# an irreducible triangle with those sides.

# Input data format:
# The program takes three positive integers as input.

# Output data format:
# The program should output "YES" or "NO" according to the problem condition.

a, b, c = int(input()), int(input()), int(input())
if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')