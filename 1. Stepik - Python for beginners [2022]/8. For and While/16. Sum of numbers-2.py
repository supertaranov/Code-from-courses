# A natural number n is given as input to the program. 
# Write a program that calculates the sum of those numbers from 1 to n (inclusive), 
# the square of which ends in 2, 5 or 8.

# Input data format:
# The program receives a natural number n as input.

# Output data format:
# The program should output a single number according to the problem condition.

# Note. If there are no such numbers in the specified range, output 0.

n = int(input())

sm = 0
for i in range(5, n + 1, 10):
    sm += i

print(sm)