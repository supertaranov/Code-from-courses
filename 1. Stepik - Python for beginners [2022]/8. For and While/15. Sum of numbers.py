# A natural number is given as input to the program n, and then n integers, each on a separate line. 
# Write a program that calculates the sum of the input numbers. 

# Input data format:
# The input to the program is a natural number n and then n integers, each on a separate line.

# Output data format:
# The program should output the sum of the given numbers.

n = int(input())

sm = 0
for _ in range(n):
    sm += int(input())
    
print(sm)