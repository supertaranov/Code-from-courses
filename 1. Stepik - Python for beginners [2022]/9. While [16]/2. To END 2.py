# The input to the program is a sequence of words, each word on a separate line. 
# The end of the sequence is the word "END" or "end" (in big or small letters, without quotes). 
# The words "END" and "end" are not part of the sequence, but only symbolize its end. 
# Write a program that outputs the members of this sequence.

# Input data format:
# The input to the program is a sequence of words, each word on a separate line.

# Output data format:
# The program should output the members of the sequence.

text = input()
while text != 'END' and text != 'end':
    print(text)
    text = input()