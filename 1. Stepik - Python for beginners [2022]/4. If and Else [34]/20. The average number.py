# Three different integers are given. Write a program that finds the average number.

# Input data format:
# The input to the program is three different integers, each on a separate line.

# Output data format:
# The program should output the average number.

# Note. The average is the number that comes second if the three numbers are sorted in ascending order.

a, b, c = int(input()), int(input()), int(input())
if (a - b) * (c - b) < 0:
    print(b)
elif (b - a) * (c - a) < 0:
    print(a)
else:
    print(c)