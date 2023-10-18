# A single string is given as input to the program. Write a program that outputs:

# the third character of this string;
# the penultimate character of this string;
# the first five characters of the string;
# the entire string except for the last two characters;
# all characters with even indices;
# all characters with odd indices;
# all characters in reverse order;
# all characters of the string through one in reverse order, starting from the last one.

# Input data format:
# The input to the program is a single string with a length greater than 5 characters.

# Output data format:
# The program must output data according to the condition. Each value is output on a separate line.

t = input()
print(t[2])
print(t[-2])
print(t[:5])
print(t[:-2])
print(t[0::2])
print(t[1::2])
print(t[::-1])
print(t[-1::-2])