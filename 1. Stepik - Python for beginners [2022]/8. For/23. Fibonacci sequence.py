# Write a program that reads the natural number n and outputs the first n numbers of the Fibonacci sequence.

# Input data format:
# The input to the program is one number n (n≤100) - the number of members of the sequence.

# Output data format:
# The program should output the members of the Fibonacci sequence separated by a space character.

# Note. Fibonacci sequence is a sequence of natural numbers, where each successive number is the sum of two previous numbers.

num = int(input())
f1 = 0
f2 = 1
for i in range(0, num):
    f1, f2 = f2, f1 + f2 
    print(f1, end=' ')