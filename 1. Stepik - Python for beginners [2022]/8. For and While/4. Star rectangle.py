# Write a program that prints a star rectangle with sizes n × 19.

# Input data format:
# A natural number n is given as input to the program.

# Output format:
# The program should output a star rectangle with dimensions n × 19.

n = int(input())
for i in range(n):
    print('*' * 19)