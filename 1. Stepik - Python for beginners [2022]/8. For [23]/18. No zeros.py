# Write a program that reads 10 numbers and outputs the product of non-zero numbers.

# Input data format
# The input to the program is 10 integers, each on a separate line.

# Output format
# The program should output the product of non-zero numbers.

# Note. It is guaranteed that at least one of the 10 numbers is non-zero.

total = 1
for i in range(10):
    num = int(input())
    if num != 0:
        total *= num
print(total)