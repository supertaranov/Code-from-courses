# A sequence of 10 integers is being processed. 
# You need to write a program that displays the number of non-negative numbers of the sequence and their product. 
# If there are no non-negative numbers, the program must display "NO". 
# The programmer was in a hurry and wrote the program incorrectly.

# Find all the errors in this program (there are exactly 4). 
# It is known that each error affects only one line and can be corrected without changing other lines.

# Note. If necessary, you can add the necessary lines of code.

count = 0
p = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p *= x
        count += 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')