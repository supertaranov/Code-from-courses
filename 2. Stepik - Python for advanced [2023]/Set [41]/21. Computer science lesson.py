# A 10-point scale is given for the computer science grades of three students. 
# Write a program that outputs a set of grades that both the first and second student have, 
# but that the third student does not.

# The format of the input data:
# The input is the grades of three students, separated by a space character (each student's grade on a separate line).

# The output format:
# The program has to output the set of grades in descending order on one line, 
# separated by spaces, according to the problem.

# Note. The student's grade is between 0 and 10 inclusive.

set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

print(*sorted(set1 & set2 - set3, reverse=True))