# Call a number interesting if its difference between the maximum and minimum digits is equal to the average digit. 
# Write a program that determines whether a number is interesting or not. 
# If the number is interesting, "The number is interesting" should be output, otherwise "The number is not interesting".

# The format of the input data:
# The input to the program is a three-digit integer.

# Output format:
# The program should print the text according to the problem.

num = int(input())
a = num // 100
b = num % 100 // 10
c = num % 10
d = max(a, b, c) - min(a, b, c)
if a + b + c - max(a, b, c) - min(a, b, c) == d:
    print('The number is interesting')
else:
    print('The number is not interesting')