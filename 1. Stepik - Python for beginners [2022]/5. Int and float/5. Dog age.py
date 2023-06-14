# The program is inputted with a number n is the number of dog years. 
# Write a program that calculates the age of a dog in human years.

# Input data format:
# The program input is a natural number - the number of years of a dog.

# Output data format:
# The program should output the dog's age in human years.

# Note. During the first two years the dog year is equal to 10.5 human years. 
# After that, each dog year equals 4 human years.

age = int(input())
if age == 1 or age == 2:
    print(age * 10.5 )
elif age > 2:
    print(age * 4 + 13 )