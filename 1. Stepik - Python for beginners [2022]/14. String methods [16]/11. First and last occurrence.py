# The program is given a string of text as input. 
# If the letter "f" occurs only once in this string, print its index. 
# If it occurs two or more times, print the index of its first and last occurrences on the same line, 
# separated by a space character. If the letter "f" does not occur in this line, print "NO".

# Input data format:
# The input to the program is a string of text.

# Output format:
# The program should output the text according to the problem condition.

s = input()
if s.count('f') == 1:
        print(s.find('f'))
elif s.count('f') >= 2:
        print(s.find('f'), s.rfind('f'))
elif s.count('f') == 0:
        print('NO')