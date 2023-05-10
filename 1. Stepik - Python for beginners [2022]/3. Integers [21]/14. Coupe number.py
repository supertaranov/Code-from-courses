# In the compartment carriage there are 9 compartments with four seats
# for passengers in each compartment. Write a program that determines 
# the number of the compartment in which there is a seat with 
# the given number (the numbering of seats is continuous, starting from 1).

# Input data format:
# The input of the program is an integer number - the seat with the given number in the car.

# Output data format:
# The program should output one number - the number of the compartment 
# in which the specified seat is located.

n = int(input())
print((n+3) // 4)