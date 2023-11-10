# The input to the program is a sequence of integers from 1 to 5, characterizing the student's grade, 
# each number on a separate line. The end of the sequence is any negative number or a number greater than 5. 
# Write a program that outputs the number of fives.

# Input data format:
# The input to the program is a sequence of numbers, each number on a separate line.

# Output data format:
# The program should output the number of fives.

num = int(input())
counter = 0
while num >= 0 and num <= 5:
    if num == 5:
        counter += 1
    num = int(input())
print(counter)