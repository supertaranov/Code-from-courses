# Write a program that determines the smallest of four numbers.

# Input data format:
# The input to the program is four integers.

# Output data format:
# The program should output the smallest of the four numbers.

num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
if num1 > num2:
        num1 = num2
if num3 > num4:
        num3 = num4
if num1 > num3:
        num1 = num3 
        
print(num1)