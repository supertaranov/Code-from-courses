# Write a program that determines whether a user is allowed to access an Internet resource or not.

# Input data format:
# The input of the program is an integer number - the age of the user.

# Output data format:
# The program should print the text "Access permitted" if the age is at least 18, 
# and "Access denied" otherwise.

age = int(input())
if age >= 18:
    print('Access permitted')
else:
    print('Access denied')