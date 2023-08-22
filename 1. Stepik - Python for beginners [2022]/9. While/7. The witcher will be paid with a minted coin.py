# Everyone knows that the witcher can defeat any monster, but his services will cost a lot. 
# In addition, the witcher does not accept bills, he only accepts minted coins. 
# In the world of the witcher there are coins with denominations of 1,5,10,25.
# Write a program that determines what is the minimum number of minted coins to pay a witch doctor.

# Input data format:
# The input to the program is one natural number - the price for the witch doctor's service.

# Output data format:
# The program should output the minimum possible number of minted coins to pay.

n = int(input())
counter = 0
while n >= 25:
    counter += 1
    n = n - 25
while n >= 10:
    counter += 1
    n = n - 10
while n >= 5:
    counter += 1
    n = n - 5
while n >= 1:
    counter += 1
    n = n - 1
print(counter)