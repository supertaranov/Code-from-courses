# The input to the program is a string consisting of the first and last name of a person separated by one space. 
# Write a program that checks that the first and last name begin with a capital letter.

# Input data format:
# The input to the program is a string.

# Output format:
# The program should output "YES" if the first and last name begin with a capital letter and "NO" otherwise.

# Note. The string contains only letters.

t = input()
if t.title() == t:
    print('YES')
else:
    print('NO')