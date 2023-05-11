# Write a program that checks that for a given four-digit number 
# the following ratio is satisfied: the sum of the first and last digits 
# is equal to the difference of the second and third digits.

# Input data format:
# The input of the program is a single positive integer four-digit number.

# Output format:
# The program should output "YES" if the ratio is true, and "NO" if it is not.

number = int(input())
d = (number % 10 )
c = (number % 100) // 10
b = (number % 1000) // 100
a = number // 1000

if a + d == b - c:
    print('YES')
else:
    print('NO')