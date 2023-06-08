# The weight of an amateur boxer is known (an integer). 
# It is known that the weight is such that the boxer can be assigned to one of three weight categories:

# Lightweight - up to 60 kg;
# The first welterweight - up to 64 kg;
# Welterweight - up to 69 kg.
# Write a program that determines in what category the boxer will compete.

# Input data format:
# A single integer number is given as an input to this program.

# Output format:
# The program should output the text - the name of the weight class.

m = int(input())

if m < 60:
    print('Lightweight')
elif m < 64:
    print('The first welterweight')
elif m < 69:
    print('Welterweight')