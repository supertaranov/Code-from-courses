# Write a program that reads a positive integer x and displays 
# a sequence of numbers x, 2x, 3x, 4x and 5x separated by three dashes.

# Input data format:
# The input to the program is a positive integer.

# Output data format:
# The program should output the text according to the task condition.

x = int(input())
print( x, x * 2, x * 3, x * 4, x * 5, sep='---' )