# A BEEGEEK online school leader and his assistant have made lists of students in their school.

# Write a program that outputs all the names of the students that the supervisor and his assistant remembered.

# Input format:
# The first line of input to the program is the names recorded by the head of the school and 
# the second line is the assistant head of the school. The surnames are indicated with a space.

# Output data format:
# The program should output all the names of the students, sorted in lexicographical order, 
# written by the headmaster and his assistant.

# Note. It is guaranteed that there are no namesakes among the BEEGEEK students.

set1 = set(input().split())
set2 = set(input().split())
print(*sorted(set1 | set2))