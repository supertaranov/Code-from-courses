# A program inputs a natural number n and then n different natural numbers, 
# each on a separate line. Write a program that outputs all the common digits 
# in ascending order of all the numbers entered.

# Input data format:
# The input to the program is a natural number ≥ 1 and then n different natural numbers, each on a separate line.

# Output data format:
# The program should output the numbers according to the condition of the problem. 
# If there are no common digits, there is no need to output anything.

n = int(input())
set1 = set(input())

for _ in range(n-1):
    set1 &= set(input()) 
print(*sorted(set1))