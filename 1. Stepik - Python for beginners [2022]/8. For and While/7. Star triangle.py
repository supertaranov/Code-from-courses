# The program receives a natural number as input n(n≥2) is the cathetus of a right-angled isosceles triangle.
# Write a program that outputs the star triangle according to the example.

# Input data format:
# The program receives one natural number as input n(n≥2).

# Output data format:
# The program should output the triangle according to the problem condition.

n = int(input())
for i in range(n):
    print((n-i) * '*')