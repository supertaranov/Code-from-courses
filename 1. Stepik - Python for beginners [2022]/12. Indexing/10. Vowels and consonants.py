# The program is given one string of Russian letters as input. 
# Write a program that determines the number of vowel and consonant letters.

# Input data format:
# The program receives one string as input.

# Output data format:
# The program should output the number of vowel and consonant letters.

# Note. In Russian 10 vowel letters (а, у, о, ы, и, э, я, ю, ё, е) and 
# 21 consonant letters (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).

text = input()
total1 = 0
total2 = 0
for i in text:
    if i in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        total1 += 1
    elif i in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        total2 += 1
print('The number of vowel letters is', total1)
print('The number of consonant letters is', total2)
