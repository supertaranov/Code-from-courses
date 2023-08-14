# Given a natural number n. Write a program that outputs the multiplication table for n (from 1 to 10 inclusive).

# Input data format:
# A natural number is given as input to the program.

# Output format:
# The program should output the multiplication table for the entered number.

# Note. Use the English letter x as the multiplication sign.

n = int(input())

for i in range(1, 11):
    print(n, 'x', i, '=', n * i)