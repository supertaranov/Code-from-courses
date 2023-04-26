# An arithmetic progression is a sequence of numbers a1, a2 ..., 
# each of which, starting from a2, is obtained from the previous one by adding to 
# it the same constant number d (the difference of the progression)

# Input data:
# The program is fed three integers:
# a1, d and n, each on a separate line.

# Output data:
# The program should output the nth term of the arithmetic progression.

a = int(input())
d = int(input())
n = int(input()) 
print( a + d * ( n - 1 ))