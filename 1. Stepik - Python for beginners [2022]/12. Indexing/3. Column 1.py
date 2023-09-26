# The program is given one string as input. 
# Write a program that outputs the elements of the string with indices 0, 2, 4, ... into a column.

# Input data format:
# The program receives one string as input.

# Output data format:
# The program should output the elements of the string with indices 0, 2, 4, ..., each on a separate line.

text = input()
for i in range(0, len(text), 2):
    print(text[i])