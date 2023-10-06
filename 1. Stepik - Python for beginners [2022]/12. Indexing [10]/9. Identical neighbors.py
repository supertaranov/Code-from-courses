# The program is given one string as input. 
# Write a program that determines how many identical neighboring characters it contains.

# Input data format:
# The program is given one string as input.

# Output data format:
# The program should output the number of identical adjacent characters.

text = input()
counter = 0
for i in range(0, len(text) -1):
    if text[i] == text[i+1]:
        counter += 1
print(counter)