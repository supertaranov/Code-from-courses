# Given a natural number n,(n≥10). Write a program that determines its maximum and minimum digits.

# Input data format:
# The input to the program is one natural number.

# Output data format:
# The program should output the maximum and minimum digits of the entered number (with an explanatory note).

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
print('Maximum digit equals', max_num)
print('Minimum digit equals', min_num)