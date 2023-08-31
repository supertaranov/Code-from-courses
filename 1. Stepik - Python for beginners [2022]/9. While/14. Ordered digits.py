# A natural number is given. 
# Write a program that determines whether the sequence of its digits is non-decreasingly ordered when viewed from right to left.

# Input data format:
# One natural number is given as input to the program.

# Output format:
# The program should output "YES" if the sequence of its digits when viewed from right to left is non-decreasing ordered and "NO" otherwise.

num = int(input())
counter = 0
while num != 0:
    last1 = num % 10
    last2 = (num % 100) // 10
    if last1 > last2:
        counter += 1
    if last1 <= last2:
        counter = counter
    num = num // 10
if counter == 1:
    print('YES')
else:
    print('NO')