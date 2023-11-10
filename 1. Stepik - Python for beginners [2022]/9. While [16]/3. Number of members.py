# The input to the program is a sequence of words, each word on a separate line. 
# The end of the sequence is one of two words: "stop" and "enough" (in small letters, without quotes). 
# These words themselves are not included in the sequence, only symbolizing its end. 
# Write a program that outputs the total number of members of this sequence.

# Input data format:
# The input to the program is a sequence of words, each word on a separate line.

# Output data format:
# The program should output the total number of members of the sequence.

text = input()
total = 0
while text != 'stop' and text != 'enough':
    num = 1
    total += num
    text = input()
print(total)