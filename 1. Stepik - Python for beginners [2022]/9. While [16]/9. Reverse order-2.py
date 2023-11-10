# A natural number is given. 
# Write a program that reverses the order of digits of the number.

# Input data format:
# One natural number is given as input to the program.

# Output data format:
# The program should output the number written in reverse order.

n = int(input())
new_n = 0

while n > 0:
    new_n = new_n * 10 + n % 10
    n //= 10
    
print(new_n)