# The program is given a string of genetic code consisting of the letters A (adenine), G (guanine), C (cytosine), and T (thymine). 
# Write a program that counts how many adenine, guanine, cytosine, and thymine are included in this string of genetic code.

# Input data format:
# The input to the program is a string of genetic code consisting of the characters A, G, C, T, a, g, c, t.

# Output data format:
# The program should output how many guanine, thymine, cytosine, adenine are included in the given genetic code string.

# Note. The string does not contain any characters other than A, G, Ts, T, a, g, ts, t.

s = input()
k = s.lower()
print('Adenine:', k.count('a'))
print('Guanine:', k.count('g'))
print('Cytosine:', k.count('c'))
print('Thymine:', k.count('t'))