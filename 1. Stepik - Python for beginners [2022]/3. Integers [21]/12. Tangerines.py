# "a" schoolchildren share "b" tangerines equally, 
# the non-dividing remainder remains in the basket. 
# How many whole tangerines will each student get? 
# How many whole tangerines will remain in the basket?

# Input data format:
# The program is given two integers for input: 
# the number of schoolchildren and the number of tangerines, each on a separate line.

# Output data format:
# The program should output two numbers: 
# the number of tangerines that each student will get, 
# and the number of tangerines that will remain in the basket, each on a separate line.

a = int(input())
b = int(input())
print( b // a )
print( b % a )