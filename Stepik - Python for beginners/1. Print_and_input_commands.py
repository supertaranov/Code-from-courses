# Task 1:
# Write a program that displays the text "Hello, World!" (without quotes).
# Note 1. The checking system will compare the result 
# of your program and the correct answer is character-by-character. 
# This means that you need to output exactly the line that is specified in the task condition.
# Note 2. The checking system uses the standard output (stdout, command print()).

print('Hello, World!')

# Task 2:
# In the popular TV series "Stay Alive" the sequence was used 
# of numbers 4 8 15 16 23 42, which brought the heroes luck and helped to hit the jackpot in the lottery. 
# Write a program that outputs a given sequence of numbers with one space between them.
# Note. The text '4 8 15 16 23 42' should not be used. 
# Use the print() command to output multiple arguments separated by commas.

q,w,e,r,t,y = 4,8,15,16,23,42
print(q,w,e,r,t,y)

# Task 3:
# Change the previous program so that each number of the sequence 
# 4 8 15 16 23 42 was printed on a separate line.
# Note. Each subsequent print() command outputs the specified text starting from a new line.

q,w,e,r,t,y = 4,8,15,16,23,42
print(q,w,e,r,t,y, sep='\n')

# Task 4:
# Write a program that outputs the specified triangle consisting of asterisks (*).

print('*')
print('*'*2)
print('*'*3)
print('*'*4)
print('*'*5)
print('*'*6)
print('*'*7)