# The program is given one number n as input. 
# Write a program that outputs a list of n letters of the English alphabet ['a', 'b', 'c', ...] in lower case.

# Input data format:
# The program is given a natural number n,1≤n≤26 as input.

# Output data format:
# The program should output the text according to the problem condition.

n = int(input())
x = list()
for i in range(n):
    x += chr(ord('a') + i)
print(x, end=' ')