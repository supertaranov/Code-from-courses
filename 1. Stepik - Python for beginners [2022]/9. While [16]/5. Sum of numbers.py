# The input to the program is a sequence of integers, each number on a separate line. 
# Any negative number is a sign of the end of the sequence, but it is not included in the sequence itself. 
# Write a program that outputs the sum of all members of the sequence.

# Input data format:
# The input to the program is a sequence of numbers, each number on a separate line.

# Output data format:
# The program should output the sum of the members of the sequence.

num = int(input())
total = 0
while num >= 0:
    total += num
    num = int(input())
print(total)