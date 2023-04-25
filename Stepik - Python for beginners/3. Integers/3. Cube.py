# Write a program that calculates the volume of a cube and the area of its full surface, 
# based on the entered value of the edge length.

# Input data format:
# The input to the program is a single integer – the length of the edge.

# Output data format:
# The program should output text and numbers according to the task condition.

a = int(input())
v = a * a * a
print('Volume =', v)
s = a * 6 * a 
print('Total surface area =', s)