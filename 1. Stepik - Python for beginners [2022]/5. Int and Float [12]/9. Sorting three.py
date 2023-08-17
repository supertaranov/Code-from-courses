# Write a program that sorts three numbers from larger to smaller.

# Input data format:
# The input to the program is three integers, each on a separate line.

# Output format:
# The program should output three numbers, each on a separate line, ordered from higher to lower.

a, b, c = int(input()), int(input()), int(input())
x = min(a, b, c)
y = max(a, b, c)
if a <= b <= c or c <= b <= a:
    print(y)
    print(b)
    print(x)
elif b <= a <= c or c <= a <= b:
    print(y)
    print(a)
    print(x)
elif b <= c <= a or a <= c <= b:
    print(y)
    print(c)
    print(x)