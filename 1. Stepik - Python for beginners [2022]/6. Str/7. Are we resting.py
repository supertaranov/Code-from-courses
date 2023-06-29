# Write a program that reads one line, then outputs "YES" if the entered line
# has a substring "Saturday" or "Sunday", and "NO" otherwise.

# Input data format:
# The program inputs one string.

# Output format:
# The program should output the text according to the problem's condition.

x = input()
if 'Saturday' in x or 'Sunday' in x:
    print('YES')
else:
    print('NO')