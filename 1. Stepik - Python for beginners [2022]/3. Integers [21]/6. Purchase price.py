# Write a program that calculates the cost of three computers consisting of a monitor, 
# a system unit, a keyboard and a mouse.

# Input data format:
# The program is fed four integers, each on a separate line, as input. 
# In the first line — the cost of the monitor, in the second line — the cost of the system unit, 
# in the third line — the cost of the keyboard and in the fourth line — the cost of the mouse.

# Output data format:
# The program should output one number – the purchase price (three computers).

display = int(input())
pc = int(input())
keyboard = int(input())
mouse = int(input())
print((display + pc + keyboard + mouse) * 3)