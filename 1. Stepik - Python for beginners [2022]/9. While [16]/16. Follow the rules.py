# A natural number is given as input to the program n. 
# Write a program that outputs the numbers from 1 to n inclusive except:
# numbers from 5 to 9 inclusive;
# numbers from 17 to 37 inclusive;
# numbers from 78 to 87 inclusive.

# Input data format:
# The program receives one natural number n as input.

# Output data format:
# The program should output the numbers according to the problem condition, each on a separate line.

# Note. Use the continue operator.

n = int(input())
for i in range(1, n+1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)