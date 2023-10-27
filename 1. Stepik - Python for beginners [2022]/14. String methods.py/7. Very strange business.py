# Jim Hopper is using a radio receiver to try to get a message to Odie. 
# He's receiving n different Morse code sequences. 
# By decoding them, he receives sequences of digits and letters of the lowercase Latin alphabet, 
# and all of Odie's messages contain the number 11, with a minimum of 3 times. 
# Help Jim determine the number of messages from Odi.

# Input data format:
# The first line contains a number n is the number of messages, in the following n lines contain Latin lowercase letters and digits.

# Output data format:
# The program should output the number of lines that contain the number of 11 minimum 3 times.

# Note: The numbers 11 need not necessarily be separated by other characters, you must count the occurrence of 
# the character sequence "11", i.e. for example in the string "111" contains one such sequence, 
# while in "1111" contains two such sequences.

n = int(input())
counter = 0
for i in range(n):
    s = input()
    if s.count('11') >= 3:
        counter += 1
print(counter)