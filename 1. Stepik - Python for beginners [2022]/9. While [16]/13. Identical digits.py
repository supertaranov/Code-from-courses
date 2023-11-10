# A natural number is given. 
# Write a program that determines whether the given number consists of identical digits.

# Input data format:
# One natural number is given as input to the program.

# Output data format:
# The program should output "YES" if the number consists of identical digits and "NO" otherwise.

num = int(input())
min_num = 9
max_num = 0
while num != 0:
    last = num % 10
    if last > max_num:
        max_num = last
    if last < min_num:
        min_num = last
    num = num // 10
if min_num == max_num:
    print('YES')
else:
    print('NO')