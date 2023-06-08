# Red, blue, and yellow are called primary colors because they cannot be obtained by mixing other colors. 
# If you mix two primary colors, you get a secondary color:

# If you mix red and blue, you get purple;
# If you mix red and yellow, you get orange;
# If you mix blue and yellow, you get green.
# Write a program that reads the names of the two primary colors to mix. 
# If the user enters anything other than the names "red", "blue" or "yellow", 
# the program should output an error message. Otherwise, 
# the program should output the name of the secondary color that will result.

# Input data format:
# The program inputs two lines, each on a separate line.

# Output format:
# The program should output the resulting mixing color or the "color error" message, 
# if the entered color is not a color.

# Note. If you mix red and red you get red, etc.

a, b = input(), input()

if a == 'red' and b == 'blue' or a == 'blue' and b == 'red':
    print('purple')
elif a == 'red' and b == 'yellow' or a == 'yellow' and b == 'red':
    print('orange')
elif a == 'blue' and b == 'yellow' or a == 'yellow' and b == 'blue':
    print('green')
elif (a == 'blue' or a == 'red' or a == 'yellow') and a == b:
    print(a)
else:
    print('color error')