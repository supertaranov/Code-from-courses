# The famous American writer Ray Bradbury has a novel "451 degrees Fahrenheit". 
# Write a program that determines what temperature on the Celsius scale corresponds 
# to the specified value on the Fahrenheit scale.

# Use the formula to translate: 
# C = 5/9(F - 32)

# Input data format:
# The input to the program is a real number of degrees on the Fahrenheit scale.

# Output data format:
# The program should output the number of degrees on the Celsius scale.

c = float(input())
print((c - 32) * 5/9)