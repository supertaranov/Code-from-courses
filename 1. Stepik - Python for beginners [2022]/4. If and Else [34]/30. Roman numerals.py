# Write a program that reads an integer and outputs the corresponding Roman numeral. 
# If the number is outside the range 1-10, the program should print the text "error".

# Input data format:
# An integer number is given as input to the program.

# Output data format:
# The program should output the text according to the problem condition.

num = int(input())
if num < 1 or num > 10:
    print('error')
elif num == 1:
    print('I')
elif num == 2:
    print('II')    
elif num == 3:
    print('III')
elif num == 4:
    print('IV')
elif num == 5:
    print('V')
elif num == 6:
    print('VI')
elif num == 7:
    print('VII')
elif num == 8:
    print('VIII')
elif num == 9:
    print('IX')
elif num == 10:
    print('X')    