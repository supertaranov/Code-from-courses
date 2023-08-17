# A sentence is given and the number of times it should be repeated. 
# Write a program that repeats the given sentence the required number of times.

# Input data format:
# The first line contains the text sentence, the second line contains the number of repetitions.

# Output data format:
# The program should output the specified text sentence the required number of times. 
# Each repetition must start from a new line.

a = input()
b = int(input())
for i in range(b):
    print(a)