# Morse code uses dashes and periods to represent numbers and letters.
# Write a program to encode a text message according to Morse code.

# Input data format:
# The input to the program is a single line - a text message.

# Output data format
# The program has to output a Morse code coded message, leaving a space between each coded character 
# (a sequence of dashes and dots).

# Note 1. Your program should ignore any characters not listed in the table.

# Note 2. Morse code was developed in the 19th century and is still in use, more than 160 years after its creation.

letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = [
    '.-', 
    '-...', 
    '-.-.', 
    '-..', 
    '.', 
    '..-.', 
    '--.', 
    '....', 
    '..', 
    '.---', 
    '-.-', 
    '.-..', 
    '--', 
    '-.', 
    '---', 
    '.--.', 
    '--.-', 
    '.-.', 
    '...', 
    '-', 
    '..-', 
    '...-', 
    '.--', 
    '-..-', 
    '-.--', 
    '--..', 
    '-----', 
    '.----', 
    '..---', 
    '...--', 
    '....-', 
    '.....', 
    '-....', 
    '--...', 
    '---..', 
    '----.'
    ]

info = dict(zip(letters, morse))
for i in input().upper():
    for key, value in info.items():
        if i in key:
            print(value, end=" ")