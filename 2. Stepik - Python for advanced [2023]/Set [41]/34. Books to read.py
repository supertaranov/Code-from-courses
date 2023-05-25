# At the end of the school year, Ruslan received a reading list for the summer. 
# Now he needs to find out which books from this list he has. 
# Ruslan's computer has a text file with all the books from his home library written in random order.
# Write a program that determines for each book in the reading list, whether Ruslan has it or not.

# The format of the input data:
# The first line of the program is inputted with a natural number 
# m is the number of books in Ruslan's library. The second line contains a natural number 
# n - the number of books in the list for the summer. Next are 
# m lines with the titles of books from the home library and 
# n lines of titles from the list for the summer.

# Output data format:
# The program should output 
# n lines, each containing the word YES if the book is found in the library, and NO if it is not.

m, n = int(input()), int(input())
home = {input() for _ in range(m)}
tusk = [input() for _ in range(n)]
for i in tusk:
    print('YES' if i in home else 'NO')