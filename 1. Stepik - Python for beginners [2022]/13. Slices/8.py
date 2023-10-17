# A string of text is given to the program as input. 
# Write a program that will cut it into two equal parts, rearrange them and display it on the screen.

# Input data format:
# A string of text is given as input to the program.

# Output format:
# The program should output the text according to the problem condition.

# Note. If the length of the string is odd, the length of the first part must be one character longer.

t = input()
n = len(t)//2 + len(t) % 2
print(t[n:] + t[:n])