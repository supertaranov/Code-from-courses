# A number n>1 is given as input to the program. 
# Write a program that outputs its smallest divisor different from 1.

# Input data format:
# One natural number n is given as input to the program.

# Output data format:
# The program should output the smallest divisor different from 1.

# Note. Use the break operator when a divisor is found.

n = int(input())
for i in range(2, n+1):
    if n % i == 0:
        print(i)
        break