# The program is given one string as input. 
# Write a program that outputs the elements of the string in reverse order in the column.

# Input data format:
# The program is given one string as input.

# Output data format:
# The program should output the elements of the string in reverse order.

text = input()
for i in range(1, len(text)+1):
    print(text[-i])