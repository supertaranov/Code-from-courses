# The program is given one string as input. 
# Write a program that outputs the message "Digit" (without quotes) if the string contains a digit. 
# Otherwise, print the message "No digit" (without quotes).

# Input data format:
# The program receives one string as input.

# Output data format:
# The program should output the text according to the problem condition.

text = input()
for i in text:
    if i in '0123456789':
        print('Digit')
        break
else:
    print('No digit')