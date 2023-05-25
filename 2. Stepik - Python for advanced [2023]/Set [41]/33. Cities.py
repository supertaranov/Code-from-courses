# Timur and Ruslan play the game of cities. They love this game and know many cities, especially Timur, 
# but by the end of the game because of their age they forget which cities have already been named.
# Write a program that reads the game and tells the kids that the next city has been renamed.

# The format of the input data:
# The first line of the program is a natural number 
# n is the number of names of the towns, the next 
# n lines enter the named cities and one more line with a new city that has just been named.

# Output data format:
# The program should output OK if the city has not yet been recalled, and REPEAT if the city has already been named.

n = int(input())
myset = {input() for _ in range(n+1)}
print('REPEAT' if len(myset)==n else 'OK')