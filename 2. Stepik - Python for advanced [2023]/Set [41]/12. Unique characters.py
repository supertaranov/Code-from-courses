# Write a program to output the total number of unique characters in all the words read, 
# case insensitive.

# Input data format:
# The first line of the program is inputted with the number n - the total number of words. 
# Next is n lines with words.

# Output data format:
# The program should output a single number - the total number of unique characters in all words, 
# not case-sensitive.

symbols = set()

for _ in range(int(input())):
    for i in input().lower():
        symbols.add(i)
        
print(len(symbols))