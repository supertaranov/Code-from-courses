# When registering on sites, you are required to enter your password twice. 
# This is done for security, because this approach reduces the possibility of incorrect password entry.
# Write a program that compares the password and its confirmation. 
# If they match, the program outputs: "Password accepted", otherwise: "Password not accepted".

# Input data format:
# The program has two strings at the input.

# Output data format:
# The program should output one string according to the problem condition.

a = input()
b = input()
if a == b:
    print('Password accepted')
else:
    print('Password not accepted')