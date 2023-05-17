# The program inputs two strings consisting of digits. 
# You need to determine if it is true that identical sets of digits were used to write these strings?

# Input format:
# You are given two strings of numbers at the input.

# Output format:
# The program should output YES if identical sets of digits were used to write the strings,
# and NO otherwise.

print('YES' if set(input()) == set(input()) else 'NO')