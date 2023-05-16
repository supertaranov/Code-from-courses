a, b, c, d = int(input()), int(input()), int(input()), int(input())
x = c - a
y = d - b
if -1 <= x <= 1 and -1 <= y <= 1:
    print('YES')
else:
    print('NO')