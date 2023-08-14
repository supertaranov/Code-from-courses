# A program is given a natural number n as input, followed by n different natural numbers of a sequence, 
# each on a separate line. Write a program that outputs the largest and second largest number of the sequence.

# Input data format:
# The program is given a natural number n≥2 and then n different natural numbers, each on a separate line.

# Output format:
# The program should output the two largest numbers, each on a separate line.

n = int(input())

max1, max2 = -1, -1

for _ in range(n):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num
        
print(max1)
print(max2)