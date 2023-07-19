# A natural number is given as input to the program n. 
# Write a program that for each of the numbers from 0 to n (inclusive) outputs the phrase: 
# "The square of the number [number] is equal to [number]" (without quotes).

# Input data format:
# The natural number n is given as input to the program.

# Output data format:
# The program should output the text according to the problem condition.

n = int(input())
for i in range(n + 1):
    print('The square of the number', i, 'is equal to', i**2 )