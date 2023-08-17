# Three lines are entered in random order. 
# Write a program to find out whether the lengths of these strings can be used to 
# construct an increasing arithmetic progression.

# Input Data Format:
# The program inputs three lines, each on a separate line.

# The output format:
# The program should print the string "YES" if the lengths of the entered words can be used to 
# construct an arithmetic progression, "NO" otherwise.

a, b, c = len(input()), len(input()), len(input())
x = max(a, b, c)
y = min(a, b, c)
z = (a + b + c) - (x + y)
if x - z == z - y:
    print('YES')
else:
    print('NO')