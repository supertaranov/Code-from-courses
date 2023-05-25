# Write a program to output the number of unique characters of each word you read, case insensitive.

# Input data format:
# The first line of the program enters the number n - the total number of words.
# This is followed by n lines of words.

# Output data format:
# The program should print on one line the number of unique characters for each word.

for i in range(int(input())):
    print(len(set(input().lower())))