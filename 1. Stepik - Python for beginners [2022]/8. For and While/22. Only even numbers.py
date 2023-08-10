# Write a program that reads a sequence of 10 integers and determines whether each of them is even or not.

# Input data format:
# The input to the program is 10 integers, each on a separate line.

# Output format:
# The program should output the string "YES" if all numbers are even and "NO" otherwise.

total = 0
counter = 0
for i in range(10):
    num = int(input())
    if num % 2 == 0:
        total += num
        counter += 1
if counter == 10:
    print('YES')
else:
    print('NO') 