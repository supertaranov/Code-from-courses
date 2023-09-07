# A sequence of 10 integers. 
# It is known that the absolute value of the input numbers does not exceed 10^6. 
# You need to write a program that displays the sum of all negative numbers in the sequence 
# and the maximum negative number in the sequence. If there are no negative numbers, the program must display "NO". 
# The programmer was in a hurry and wrote the program incorrectly.

# Find all the errors in this program (there are exactly 5). 
# It is known that each error affects only one line and can be corrected without changing other lines.

# Note 1. Number x does not exceed in absolute value 10^6 if -10^6 ≤ x ≤ 10^6.
# Note 2. If necessary, you can add the necessary lines of code.

mx = 0
s = 0
for i in range(11):
    x = int(input())
    if x < 0:
        s = x
    if x > mx:
        mx = x
print(s)
print(mx)