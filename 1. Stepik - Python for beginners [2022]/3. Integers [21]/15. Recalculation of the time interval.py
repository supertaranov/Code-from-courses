# Write a program to convert the time interval value, 
# given in minutes, into a value expressed in hours and minutes.

# The format of the input data:
# The program is inputted with an integer number - the number of minutes.

# Output data format:
# The program should print the text according to the problem's statement.

minutes = int(input())
print(minutes , 'minutes - it is' , (minutes // 60) , 'hour' , (minutes % 60) , 'minutes.')