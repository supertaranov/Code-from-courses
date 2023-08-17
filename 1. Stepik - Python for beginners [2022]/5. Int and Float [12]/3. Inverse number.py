# Write a program that reads one number from the keyboard and prints the inverse of it. 
# If the number entered from the keyboard is zero, print "There is no inverse number" (without the quotes).

# Input data format:
# The program inputs a single real number.

# Output format:
# The program should print a real number that is the reverse of the given number, 
# or the text as per the problem's condition.

num = float(input())
if num == 0:
    print('There is no inverse number')
else:
    print(num ** (-1))