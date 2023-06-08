# Write a program that takes a number as input and outputs "YES" or "NO" depending on the conditions.

# Conditions:
# if the number is odd, output "YES";
# if the number is even within the range of 2 to 5 (inclusive), output "NO";
# if the number is even within the range of 6 to 20 (inclusive), output "YES";
# if the number is even and greater than 20, output "NO".

# Input data format:
# A natural number is given as an input to the program.

# Output data format:
# The program should output the text according to the problem condition.

num = int(input())
if num % 2 != 0 or 6 <= num <= 20 and num % 2 == 0:
    print('YES')
elif 2 <= num <= 5 and num % 2 == 0 or num > 20 and num % 2 == 0:
    print('NO')