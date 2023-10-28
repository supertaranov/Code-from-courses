# A string of text is given as input to the program. Write a program that counts the number of digits in this string.

# Input data format:
# A string of text is given as input to the program.

# Output data format:
# The program should output the number of digits in the given string.

s = input()
counter = 0
for i in range(10):
      counter += s.count(str(i))
print(counter)