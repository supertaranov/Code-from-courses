# Three students are given a 10-point scale for their grades in physics. 
# Write a program that outputs a set of grades for the third student that does 
# not occur in either the first or second student.

# Input Data Format:
# The input is the grades of three students, separated by a space character (each student's grade on a separate line).

# The output format:
# The program has to print the set of grades, in descending order, on one line, 
# separated by spaces, according to the problem.

# Note. The student's grade is between 0 and 10 inclusive.

set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

print(*sorted(set3 - (set1 | set2), reverse=True))