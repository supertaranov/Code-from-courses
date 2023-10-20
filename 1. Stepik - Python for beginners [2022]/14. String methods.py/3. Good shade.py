# A string of text is given as input to a program. 
# Write a program that determines whether the shade of the text is good or not. 
# The text has a good hue if it contains the substring "good" in all possible registers.

# Input data format:
# The input to the program is a string of text.

# Output format:
# The program should output "YES" if the text is good and "NO" otherwise.

# Note. Text containing good, GOOD, Good, gOOD, etc. has a good connotation.

t = input()
t = t.lower()
if 'good' in t:
    print('YES')
else:
    print('NO')