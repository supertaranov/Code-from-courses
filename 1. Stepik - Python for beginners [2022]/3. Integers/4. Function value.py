# Write a program for calculating the value of the function
# f(a,b) = 3(a + b)**3 +275b**2 − 127a − 41
# by the entered integer values a and b.

# Input data format:
# The program is fed two integers, each on a separate line, as input. 
# In the first line — the value of a, in the second line — the value of b.

# Output data format:
# The program should output the value of the function from the entered numbers a and b.

a = int(input())
b = int(input())
s1 = (3*(a+b)*(a+b)*(a+b)) + ((275 * b) * b) - (127 * a) - 41
print(s1)