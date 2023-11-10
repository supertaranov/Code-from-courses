# A string is given as input to the program. 
# Write a program that counts the number of alphabetic characters in lower case.

# Input data format: 
# A string is given as input to the program.

# Output data format:
# The program should output the number of alphabetic characters in lower case.

s = input()
cnt_al_lower = 0

for el in s:
    if el != el.upper():
        cnt_al_lower += 1
        
print(cnt_al_lower)