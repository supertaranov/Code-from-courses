# A sequence of 7 integers is received for processing. 
# It is known that the input numbers in absolute value do not exceed 10^6. 
# You need to write a program that calculates and outputs the sum of all even numbers in 
# the sequence or 0 if there are no even numbers in the sequence. 
# The programmer was in a hurry and wrote the program incorrectly.

# Find all the errors in this program (there are exactly 4). 
# It is known that each error affects only one line and can be corrected without changing other lines.

# Note 1. The number x does not exceed in absolute value 10^6 if -10^6 ≤ x ≤ 10^6 .
# Note 2. If necessary, you can add the necessary lines of code.

s = 0 #error
for i in range(1, 8): #error
    n = int(input()) #error
    if n % 2 == 0: #error
        s = s + n 
print(s)