# The Tribonacci sequence
# Write a program that reads a natural number n and outputs the first 
# n numbers of the Tribonacci sequence.

# Input Data Format:
# The input to the program is one number n (n≤100) - the number of members of the sequence.

# Output data format:
# The program should output the members of the Tribonacci sequence, separated by a space character.

# Note. A Tribonacci sequence is a sequence of natural numbers, 
# where each successive number is the sum of the previous three: 1, 1, 1, 3, 5, 9, 17, 31, 57, 105 ...

n = int(input())
t1 = t2 = t3 = 1

for i in range(n):
    print(f1, end=' ')
    f1, f2, f3 = f2, f3, f1 + f2 + f3