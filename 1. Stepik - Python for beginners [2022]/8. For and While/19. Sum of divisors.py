# A natural number n is given as input to the program. Write a program that calculates the sum of all its divisors.

# Input data:
# The program is given a natural number n.

# Output data:
# The program should output a single number according to the problem condition.

# Note. The function of counting the sum of all divisors of a number is very important in number theory.

n = int(input())

total = 0
for i in range (1, n + 1):
    if n % i == 0:
        total += i
        
print(total)