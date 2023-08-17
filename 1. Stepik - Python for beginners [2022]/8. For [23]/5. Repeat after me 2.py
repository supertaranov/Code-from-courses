# Write a program that reads one line of text and outputs 10 lines numbered 0 to 9, each with the specified line of text.

# Input Data Format:
# One line of text is given as input to the program.

# Output Format:
# The program should output ten lines according to the problem condition.

a = input()
for i in range(10):
    print(i, a)