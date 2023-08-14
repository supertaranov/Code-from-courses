# The program receives a sequence of words as input, each word on a separate line. 
# The end of the sequence is the word "END" (without quotes). 
# The word "END" itself is not included in the sequence, only symbolizing its end. 
# Write a program that outputs the members of this sequence.

# Input data format:
# The input to the program is a sequence of words, each word on a separate line.

# Output data format:
# The program should output the members of the sequence.

text = input()
while text != 'END':
    print(text)
    text = input()