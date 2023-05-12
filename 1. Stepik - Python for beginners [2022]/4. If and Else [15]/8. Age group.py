# Write a program that tells you which age group the user belongs to, based on the entered age:
# up to and including 13 - childhood;
# 14 to 24 - youth;
# from 25 to 59 - maturity;
# over 60 - old age.

# Input data format:
# The program inputs a single integer number - the user's age.

# Output data format:
# The program should output the name of the age group.

number = int(input())
if number <= 13:
    print('childhood')
if 14 <=  number <= 24:
    print('youth')
if 25 <=  number <= 59:
    print('maturity')
if number >= 60:
    print('old age')