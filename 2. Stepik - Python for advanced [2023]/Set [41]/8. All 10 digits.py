# The input to the program is two strings consisting of digits. 
# You need to determine if it is true that all ten digits are used in writing these two strings.

# Input format:
# The input is two strings consisting of digits.

# Output format:
# The program should print YES if all ten digits are used, and NO otherwise.

numbers = set(input() + input())
print('YES' if len(numbers) == 10 else 'NO')