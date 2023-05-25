# Every student enrolled in the BEEGEEK online school takes either math, computer science, or both. 
# The head of the school has lists of students studying each subject. 
# By chance, the lists of all the students are mixed up.

# Write a program that allows the principal to find out how many students are studying just one subject.

# Input Data Format:
# The first two lines of input to the program are numbers 
# m and n - the numbers of students studying mathematics and computer science, respectively. Then we have 
# m+n lines - the names of students studying mathematics and computer science, in any order.

# Output data format:
# The program should print the number of students who study only one subject. 
# If there are no such students, then output NO.

# Note. It is guaranteed that there are no namesakes among the BEEGEEK students.

m, n = int(input()), int(input())
list1 = [input() for _ in range(m+n)]
set1 = set(list1)

for i in list1:
    if list1.count(i) > 1:
        set1.discard(i)
print(len(set1) or 'NO')