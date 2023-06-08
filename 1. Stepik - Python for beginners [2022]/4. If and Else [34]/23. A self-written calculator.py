# Write a program that reads from the keyboard two integers and a string. 
# If the string is one of four mathematical operations (+, -, *, /), 
# print the result of applying this operation to the previously entered numbers, 
# otherwise print "Invalid operation". If the user wants to divide by zero, print the text "Can't divide by zero!"

# Input data format:
# The program inputs two integers, each on a line, and a string.

# Output data format:
# You should print the result of an operation applied to the numbers you entered, 
# or a corresponding text if the operation is wrong or if it is divided by zero.

a, b = int(input()), int(input())
s = input()
if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s == '/':
    if b == 0:
        print("Can't divide by zero!")
    else:
        print(a / b)
else:
    print("Invalid operation")