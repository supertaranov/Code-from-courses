# On cell phones, text messages can be sent using the numeric keypad. 
# Because each key has multiple letters associated with it, most letters require multiple keystrokes. 
# Pressing a number once generates the first character specified for that key. 
# Pressing the digit 2,3,4 or 5 generates a second, third, fourth or fifth key character.

# 1 .,?!:
# 2 ABC
# 3 DEF
# 4 GHI
# 5 JKL
# 6 MNO
# 7 PQRS
# 8 TUV
# 9 WXYZ
# 0 space (space)
# Write a program that displays the keystrokes required for the entered message.

# Input format:
# The program inputs a single line, a text message.

# Output format:
# The program should output the keystrokes needed for the entered message.

# Note 1. Your program should handle both uppercase and lowercase letters.

# Note 2. Your program should ignore any characters not listed in the table above.

keyboard = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}

for i in input().upper():
    for key, value in keyboard.items():
        if i in value:
            print(key * (value.index(i) + 1), end="")