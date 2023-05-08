# Write a program that displays a list of good and excellent students in your class.

# Input data format:
# The program is inputted with a natural number n, 
# followed by n lines with the last name of the student and his grade on each of them.

# Output data format:
# The program should first output all of the entered lines with the students' names 
# and grades in the same order. This is followed by a blank line, 
# and then the rows with the names and grades of good and excellent students (in the same order).

# Note 1. A student's grade is a natural number from 1 to 5.
# Note 2. It is guaranteed that there is at least one good student in the class with a grade of 4, 
# or an honors student who gets 5.

marks = []
for i in range(int(input())):
    marks.append(tuple(input().split()))
    print(*marks[i])
print()

for mark in marks:
    if mark[1] in '45':
        print(*mark)