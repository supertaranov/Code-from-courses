# Two natural numbers m and n (m ≤ n) are given. 
# Write a program that outputs all numbers from m to n inclusive, satisfying at least one of the conditions:
# the number is a multiple of 17;
# the number ends in 9;
# the number is a multiple of 3 and 5 at the same time.

# Input data format:
# Two natural numbers m and n ( m≤n), each on a separate line.

# Output data format:
# The program should output numbers according to the problem condition.

# Note. If there are no numbers satisfying the condition, there is no need to output anything.

m, n = int(input()), int(input())

for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
        print(i)