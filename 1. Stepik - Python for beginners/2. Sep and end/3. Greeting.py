# Write a program that greets the user by outputting the word "Hello" (without quotes), 
# followed by a comma and a space, followed by the entered name and an exclamation mark.

# Input data format:
# The program is provided with one line for input — the user name.

# Output data format:
# The program should output the text according to the task condition.

# Note 1. There should be no spaces before the exclamation mark.
# Note 2. Use the optional 'end' parameter.

name = input()
print('Hello', name, sep=', ', end='!')