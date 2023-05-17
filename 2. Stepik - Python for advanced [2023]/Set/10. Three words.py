# The input to the program is a string of three words. 
# Is it true that the same set of letters was used to write all three words?

# Input format:
# The program input is a string of three words.

# Output format:
# The program should output YES if the same set of letters was used to write all three words, 
# and NO otherwise.

a, b, c = input().split()
print("YES" if set(a) == set(b) == set(c) else "NO")