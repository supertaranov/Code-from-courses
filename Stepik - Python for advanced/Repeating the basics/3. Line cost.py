# Task 3
# A line of text is given. Write a program to calculate the cost of a string, 
# based on the fact that any one character (including a space) it costs 60 cents. 
# Give the answer in dollars and cents according to the examples.

# Input data format:
# A line of text is supplied to the program as input.

# Output data format:
# The program should output the cost of the line.

length = str(input())
result = len(length) * 60
dollar = result // 100 
cent = result % 100
print(f"{dollar} dollar {cent} cent")