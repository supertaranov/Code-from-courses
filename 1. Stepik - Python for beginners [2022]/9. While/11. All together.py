# Given a natural number. Write a program that calculates:
# the sum of its digits;
# the number of digits in it;
# the product of its digits;
# the arithmetic mean of its digits;
# its first digit;
# sum of its first and last digits.

# Input data format:
# The input to the program is one natural number.

# Output data format:
# The program should output the values of the specified quantities in the specified order.

num = int(input())
total = 0
counter = 0
summa = 1
last = num % 10
while num != 0:
    first = num % 10
    total += first
    counter += 1
    summa *= first
    num = num // 10
print(total)
print(counter)
print(summa)
print(total / counter)
print(first)
print(first + last)