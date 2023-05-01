# Write a program that reads an integer, 
# after which the next and previous integer with explanatory text are displayed on the screen.

# Input data format:
# The input to the program is an integer.

# Output data format:
# The program should output the text according to the task condition.

a = int(input())
b = a + 1
c = a - 1
print('Following the number', a, 'number:', b )
print('For a number', a, 'previous number:', c )