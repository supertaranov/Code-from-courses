# A string of text is given to the program as input. 
# Write a program that checks if the string ends with the substring .com or .ru.

# Input data format: 
# A string of text is given as input to the program.

# Output format:
# The program should output "YES" if the input string ends with a .com or .ru substring and "NO" otherwise.

s = input()
if s.endswith('.com') == True or s.endswith('.ru') == True:
    print('YES')
else:
    print('NO')