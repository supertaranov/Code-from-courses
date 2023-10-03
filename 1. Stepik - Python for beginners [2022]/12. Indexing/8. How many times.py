# The program is given one string as input. 
# Write a program that determines how many times + and * characters occur in the string.

# Input data format:
# The program receives one string as input.

# Output data format:
# The program should output how many times the characters + and * occur in the string.

text = input()
total1 = 0
total2 = 0
for i in text:
    if i in '+':
        total1 += 1
for j in text:
    if j in '*':
        total2 += 1
print('Symbol + occurs', total1, 'times')
print('Symbol * occurs', total2, 'times')