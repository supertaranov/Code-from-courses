# A natural number n is given as input to the program. Write a program to calculate the familiar sum.

# Input data:
# The program receives a natural number as input n.

# Output data:
# The program should output a single number according to the problem condition.

n = int(input())

f = 0
for i in range(1, n + 1):
    f += (-1) ** (i + 1) * i
    
print(f)