# A string of text is given as input to the program. 
# Write a program that displays the character that appears most often.

# Input data format:
# The input to the program is a string of text. 
# The text can contain lowercase and uppercase letters of the English and Russian alphabet, as well as numbers.

# Output data format:
# The program should output the character that appears most often.

# Note 1. If there is more than one such character, the last character in order should be output.
# Note 2. Distinguish between uppercase and lowercase letters, as well as letters of the Russian and English alphabets.

s = input()
m = 0
b = 0
for i in s:
     if s.count(i) >= m:
            m = s.count(i)
            b = i
print(b)