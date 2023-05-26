# Write a program that displays information about the course based on the course number. 

# Course Number (key) Classroom Number (value) Teacher (value) Time (value)
# CS101 3004 Hines 8:00
# CS102 4501 Alvarado 9:00
# CS103 6755 Rich 10:00
# NT110 1244 Burke 11:00 a.m.
# CM241 1411 Lee 13:00

# Input data format:
# The program inputs a single line - the course number.

# Output data format:
# The program should output the course number, then the classroom number, the instructor's name, 
# and the time of the course according to the examples.

# Note 1: Use a dictionary instead of a conditional statement.

# Note 2. Use the format() string method or f-string method for convenient output.

dict1 = {'CS101': {'audience_number': '3004', 'teacher': 'Хайнс', 'time': '8:00'}, 
'CS102': {'audience_number': '4501', 'teacher': 'Альварадо', 'time': '9:00'}, 
'CS103': {'audience_number': '6755', 'teacher': 'Рич', 'time': '10:00'}, 
'NT110': {'audience_number': '1244', 'teacher': 'Берк', 'time': '11:00'}, 
'CM241': {'audience_number': '1411', 'teacher': 'Ли', 'time': '13:00'}}

str1 = input()
if str1 in dict1:
    print("{}: {}, {}, {}".format(str1, *dict1[str1].values()))