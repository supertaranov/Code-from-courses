# A 10-point scale is given for the biology grades of three students. 
# Write a program that outputs the set of grades that do not occur in any of the three students.

# Input Data Format:
# The input is the grades of three students, separated by a space character
# (each student's grade on a separate line).

# The output format
# The program has to output the set of grades in ascending order on one line, 
# eparated by spaces, according to the problem.

# Note. The student's grade is in the range from 0 to 10 inclusive.

set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

print(*sorted(set(range(11)) - set1 - set2 - set3))