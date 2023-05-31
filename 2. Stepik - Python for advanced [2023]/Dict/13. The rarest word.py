# The program inputs a string of text. 
# Write a program that outputs the word that occurs most rarely, case insensitive. 
# If there are several such words, output the one that is less in lexicographical order.

# The format of the input:
# The input for the program is a line of text.

# The output format:
# The program has to output the word (in lower case) that occurs the least often.

# Note 1. The program must not be case sensitive, the words apple and Apple should be treated as equal.

# Note 2. A word is a sequence of letters. 
# Apart from words there may be spaces and punctuation marks .,!?:;- which should be ignored. 
# There are no other characters in the text.


# Creating a list. Immediately remove unnecessary characters, divide into words and save in lowercase
words = [word.lower().strip('.,;:-?!') for word in input().split()]
# Create a dictionary for word counting in text
result = {}
# Create a dictionary where we put the answer
result2 = {} 

# do a word count
for i in words: 
    # if there is no word, then value = 0 otherwise add +1
    result[i] = result.get(i, 0) + 1 
    
# find out the minimum value of the repeating     
minimum = min(result.values()) 
for i, j in result.items(): 
    # the loop compares the values from result1 with the found minimum
    if j == minimum:    
        # the key and the minimum value are transferred to the new dictionary
        result2[i] = j
# we print the minimum key according to the condition
print(min(result2))  