# The input to the program is a string of digits. Write a program that counts the sum of digits of this string.

# Input data format:
# The program receives one string of digits as input.

# Output data format:
# The program should output the sum of digits of the given string.

n = int(input())
total = 0
while n > 0:
    last_digit = n % 10
    total += last_digit
    n = n // 10
print(total)