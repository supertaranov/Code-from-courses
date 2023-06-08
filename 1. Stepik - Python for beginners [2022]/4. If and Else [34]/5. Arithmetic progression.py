# Write a program that determines whether three given numbers (in the order given) 
# are consecutive members of an arithmetic progression.

# Input Data Format:
# The program inputs three numbers, each on a separate line.

# Output format:
# The program should print "YES" or "NO" (without the quotes), according to the problem statement. 

num1, num2, num3 = int(input()), int(input()), int(input())
if (num2 - num1) + num2 == num3:
    print('YES')
else:
    print('NO')