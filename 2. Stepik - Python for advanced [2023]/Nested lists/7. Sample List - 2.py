# The input to the program is given the number n. 
# Write a program that creates and outputs a line-by-line nested list consisting of n lists.

# Input data format:
# The input to the program is a natural number n.

# Output data format:
# The program should output the specified nested list line by line.

n = int(input())
my_list = []

for i in range(1, n + 1):
    elem = [i for i in range(1, i + 1)]
    my_list.append(elem)
print(*my_list, sep='\n')