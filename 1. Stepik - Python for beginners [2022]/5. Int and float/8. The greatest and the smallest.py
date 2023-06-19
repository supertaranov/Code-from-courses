# Write a program that finds the smallest and largest of five numbers.

# Input data format:
# The input to the program is five integers, each on a separate line.

# Output Data Format:
# The program should print the smallest and largest numbers with an explanatory caption.

a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
x = min(a, b, c, d, e)
y = max(a, b, c, d, e)
print('The smallest number =', x )
print('The largest number =', y ) 