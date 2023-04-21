# Write a func(num1, num2) function that takes two natural numbers
# num1 and num2 as arguments and returns True if num1 is divisible by num2 and False otherwise.

# The output of the program should be "divided" 
# (if the func() function returned True) and "not divided" (if the func() function returned False).

def func(num1, num2):
    return num1 % num2 == 0

num1, num2 = int(input()), int(input())

if func(num1, num2):
    print('divided')
else:
    print('not divided')