# A natural number is given. Write a program that outputs its digits in a column in reverse order.

# Input data format: 
# The program receives one natural number as input.

# Output data format:
# The program should output the digits of the input number in reverse order in a column.

n = int(input())

while n > 0:
    print(n % 10)
    n //= 10