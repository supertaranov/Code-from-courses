# Write a program that uses exactly three for loops to print the following sequence of characters:

# AAA
# AAA
# AAA
# AAA
# AAA
# AAA
# BBBB
# BBBB
# BBBB
# BBBB
# BBBB
# E
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# G

# Output data format
# The program must output the specified sequence of characters.

for i in range(6):
    print('AAA')
for i in range(5):    
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')