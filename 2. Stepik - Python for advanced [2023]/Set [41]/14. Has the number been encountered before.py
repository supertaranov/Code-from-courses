# This program inputs a line of text containing numbers. 
# For each number print the word YES (on a separate line) 
# if the number has occurred before in the sequence, or NO if it has not.

# The format of the input:
# At the input of the program you will get a line of text, containing numbers, 
# separated by a space character.

# Output format:
# The program should print the text according to the problem statement.

# Note. The leading zeros in the numbers should be ignored.

numbers = [int(i) for i in input().split()]
myset = set()

for i in numbers:
    if i in myset:
        print('YES')
    else:
        print('NO')
        myset.add(i)