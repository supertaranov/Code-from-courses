# Two numbers a and b are given to the program as input. 
# Write a program that for each code value in the range from a to b (inclusive), 
# outputs the corresponding character from the Unicode character table. b (inclusive), 
# outputs the corresponding character from the Unicode character table.

# Input data format:
# The input to the program is two natural numbers, each on a separate line.

# Output data format:
# The program should output the text according to the problem condition.

a = int(input())
b = int(input())
for i in range(a,b+1):
    print(chr(i), end=' ')