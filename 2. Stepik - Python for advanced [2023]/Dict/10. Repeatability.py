# Complete the above code so that the result variable stores a dictionary that counts 
# the number of occurrences of each character in the string text.

# Note. There is no need to print the contents of the result dictionary.

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}
for s in text:
    result[s] = result.get(s, 0) + 1