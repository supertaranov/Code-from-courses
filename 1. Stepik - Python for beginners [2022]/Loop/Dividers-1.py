# The input to the program is two natural numbers a and b (a< b). 
# Write a program that finds a natural number from the interval [a;b] with the maximum sum of divisors.

# Input data format:
# The program inputs two numbers, each on a separate line.

# Output data format:
# You have to print two numbers on one line, separated by a space: 
# the number with the maximal sum of divisors and the sum of its divisors.

# Note. If there are several such numbers, print the largest of them.

a, b = int(input()), int(input())
# will be equal to the maximal sum of divisors
sum_count = 0
# will be equal to the maximal value which has the largest 
max_x = 0
for x in range(a, b + 1):
    # hereafter we do the zeroing of the divisors counter
    count = 0
    # We need this loop to find the number divisors for each number x
    for i in range(1, b+1):
        # we check all numbers in the range [a;b] and 
        # if they are divisors of this number and the remainder of the division is zero
        if x % i == 0:
            count += i
            # if the sum of divisors of the given number is greater than the maximal sum of divisors
            if count >= sum_count:
                # we equate the maximum sum of the divisors to the sum of the divisors of this number
                sum_count = count
                # we equate the number that has the maximal number of divisors to the variable
                # of the maximal number of divisors so that we can print it
                max_x = x

print(max_x,  sum_count)