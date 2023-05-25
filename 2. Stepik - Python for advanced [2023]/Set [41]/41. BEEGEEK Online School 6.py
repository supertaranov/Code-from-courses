# The head of the BEEGEEK online school wanted to know which of his students had attended all of their lessons 
# since the beginning of the school year. For each lesson, there is a sheet with a list of students who were present.

# Write a program that determines the names of the students who were present at all lessons.

# Input Data Format:
# The first line of the input gives the number m is the number of lessons since the beginning of the school year. 
# Next comes m blocks of lines, describing the sheets with the surnames. 
# The first line of each block contains the number of surnames n i , 
# followed by n i lines with the names of those who were on the i-th lesson.

# Output data format:
# The program should output the names of the students who were in all the lessons, 
# sorted in lexicographical order. Each surname has to be written on a separate line.

# Note 1. It is guaranteed that there are no names of the same name among the BEEGEEK students.

# Note 2. It is guaranteed that at least one student was in all classes.

m = int(input())
n = int(input())
set1 = set([input() for _ in range(n)])
set2 = set()

if m == 1:
    print(*sorted(set1), sep='\n')
else:
    for i in range(m-1):
        for j in range(int(input())):
            set2.add(input())
        set1.intersection_update(set2)
        set2.clear()
    print(*sorted(set1), sep='\n')