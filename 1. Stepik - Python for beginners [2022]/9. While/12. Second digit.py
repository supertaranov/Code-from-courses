# Given a natural number n(n>9). 
# Write a program that determines its second (from the beginning) digit.

# Input data format:
# The program receives as input one natural number consisting of at least two digits.

# Output data format:
# The program should output its second (from the beginning) digit.

num = int(input())
num2 = num
while num != 0:
    first = num % 10
    num = num // 10
while num2 != first:
    second = num2 % 10
    num2 = num2 // 10
print(second)