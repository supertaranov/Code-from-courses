# The mathematics grades of three students in on a 10-point scale. 
# Write a program that outputs grades that occur in no more than two students.

# Input format:
# The input is the grades of three students, separated by a space character
# (each student's grade on a separate line).

# The output format:
# The program has to output the set of grades in ascending order on one line, 
# separated by spaces, according to the problem.

# Note. The student's grade ranges from 0 to 10 inclusive.

set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

print(*sorted((set1 | set2 | set3) - (set1 & set2 & set3)))