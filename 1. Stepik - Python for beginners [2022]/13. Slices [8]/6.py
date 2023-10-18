# A single string is given as input to the program. Write a program that outputs:

# the total number of characters in the string;
# the original string repeated 3 times;
# the first character of the string;
# the first three characters of the string;
# the last three characters of the string;
# the string in reverse order;
# string with the first and the last character deleted.

# Input data format:
# The input to the program is a single string whose length is greater than 3 characters.

# Output data format:
# The program must output data according to the condition. Each value is output on a separate line.

text = input()
print(len(text))
print(text*3)
print(text[0])
print(text[0:3])
print(text[-3:])
print(text[::-1])
print(text[1:-1])