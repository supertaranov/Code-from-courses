# Every student enrolled in the BEEGEEK online school studies either math, computer science, or both. 
# The school leader has a list of students in each subject.

# Write a program that allows the principal to find out how many students are studying just one subject.

# The format of the input data:
# The first two lines of input are numbers m and n - the numbers of students 
# studying mathematics and computer science, respectively. Then we have 
# m lines are the names of students who study mathematics and 
# n lines with the names of students who study computer science.

# Output data format:
# The program should print the number of students who study only one subject. 
# If there are no such students, then output NO.

# Note. It is guaranteed that there are no namesakes among the BEEGEEK students.

m, n = int(input()), int(input())
mathematics_pupil = {input() for _ in range(m)}
informatics_pupil = {input() for _ in range(n)}
print(len(mathematics_pupil ^ informatics_pupil) or 'NO')