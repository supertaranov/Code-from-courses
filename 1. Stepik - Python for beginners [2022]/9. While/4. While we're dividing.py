# The input to the program is a sequence of integers divisible by 7, each number on a separate line. 
# The end of the sequence is any number that is not divisible by 7 
# (this number itself is not included in the sequence, only symbolizing its end). 
# Write a program that outputs the members of this sequence.

# Input data format:
# The input to the program is a sequence of numbers, each number on a separate line.

# Output data format:
# The program should output the members of the sequence.

num = int(input())
while num % 7 == 0:
    print(num)
    num = int(input())