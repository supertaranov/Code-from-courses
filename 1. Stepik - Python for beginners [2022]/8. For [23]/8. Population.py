# The program is given three natural numbers m,p,n as input:
# m: starting number of organisms;
# p: average daily increase in %;
# n: number of days to reproduce.

# Write a program that predicts the population size of a population of organisms. 
# The program should output the population size on each day from 1 and ending with nth day.

# Input Data Format:
# The program is given three natural numbers as input.

# Output data format:
# The program should output the text according to the problem condition.

m,p,n = float(input()), float(input()), int(input())
for i in range(n):
    print(i + 1,  m * (p / 100 + 1) ** i)