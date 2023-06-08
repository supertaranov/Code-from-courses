# There are two segments on the number line: 
# [a1; b1] and [a2; b2]. Write a program that finds their intersection.

# The intersection of two segments can be:
# - segment;
# - point;
# - an empty set.

# Input data format:
# The input to the program is 4 integers 
# a1, b1, a2, b2, each on a separate line. 
# It is guaranteed that a1 < b1 and a2 < b2. 

# Output data format:
# The program should display the boundaries of the segment that is an intersection, 
# either a common point or the text "empty set".

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input()) 
if min(b1, b2) < max(a1, a2): 
    print('empty set')
elif min(b1, b2) == max(a1, a2):
    print(min(b1, b2))
else:
    print(max(a1, a2), min(b1, b2))