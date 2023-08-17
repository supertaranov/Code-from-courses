# We will consider an email address correct if it contains the dog (@) symbol and the period. 
# Write a program that checks if the email address is correct.

# Input data format:
# The only input line is an email address.

# Output data format:
# The program outputs the "YES" string if the email address is correct, and the "NO" otherwise.

# Note. The presence of @ and . characters is not sufficient to make the e-mail address correct, 
# but their absence is guaranteed to result in an invalid e-mail address.

x = input()
y = len(x)
if '@' in x and '.' in x and y > 3:
    print('YES')
else:
    print('NO')