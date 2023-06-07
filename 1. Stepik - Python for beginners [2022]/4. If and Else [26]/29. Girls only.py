# A soccer team is recruiting girls from 10 to 15 years old, inclusive. 
# Write a program that asks for the age and gender of an applicant using 
# the letters m (for male) and f (for female) and determines whether the applicant 
# is suitable to join the team or not. If the applicant fits, print "YES", otherwise print "NO".

# The format of the input:
# The input is a natural number - the age of the applicant and a letter denoting his gender m (male) or f (female).

# Output format:
# The program should output the text according to the problem's condition.

num = int(input())
gender = input()
if 10 <= num <= 15 and gender == 'f':
    print('YES')
else:
    print('NO')