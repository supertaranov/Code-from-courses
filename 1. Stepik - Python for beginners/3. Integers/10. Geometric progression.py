# Input data:
# Three integers are supplied to the input of the program: 
# b1, q and n, each on a separate line.

#Output data:
#The program should output the n-term of the geometric progression.

b1 = int(input())
q = int(input())
n = int(input())
s = ( b1 * ( q ** (n - 1 )))
print(s)