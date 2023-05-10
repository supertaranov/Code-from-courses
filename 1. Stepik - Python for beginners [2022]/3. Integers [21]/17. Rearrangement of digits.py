# A three-digit number is given abc in which all digits are different. 
# Write a program that outputs six numbers formed by rearranging the digits of a given number.

# Input data format:
# The input to the program is a positive three-digit integer with all the digits being different.

# Output format:
# The program should output six numbers formed by shuffling the digits of 
# a given number in the following order: abc,acb,bac,bca,cab,cba.

num = int(input())
c = num % 10
b = (num % 100) // 10
a = num // 100
print(a, b, c, sep="")
print(a, c, b, sep="")
print(b, a, c, sep="")
print(b, c, a, sep="")
print(c, a, b, sep="")
print(c, b, a, sep="")