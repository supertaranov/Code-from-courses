# As you know, mathematicians are strange people. Timur, the author of this course, is no exception. 
# Every day Timur solves exactly two difficult math problems. 
# Solving the first problem, he writes down on the first piece of paper all the numbers that appear in it. 
# Then he pauses and takes on the second problem. Then he writes on the second sheet of paper all the numbers 
# that appear in it. After that, he takes another sheet and writes on it all the matching numbers from 
# the first two sheets. If there are such numbers, the day is successful, if there are no common numbers, 
# Timur considers the day a failure.

# Write a program that finds the common numbers of two pieces of paper or tells you that the day is bad 😏.

# Input data format:
# The program inputs two lines of numbers: the first line contains the numbers from the first leaflet, 
# the second from the second leaflet.

# Output format:
# The program should output the numbers on both sheets in descending order, 
# or the word combination BAD DAY if there are no such numbers.

set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
print(*sorted(set1.intersection(set2), reverse=True) if len(set1.intersection(set2)) > 0 else ('BAD DAY',))

