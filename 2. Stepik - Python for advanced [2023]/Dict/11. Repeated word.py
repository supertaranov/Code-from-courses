# Complete the above code so that it outputs the most frequent word of the string s. 
# If there are several such words, it should output the one that is less in lexicographical order.

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

# Create a dictionary for word counting in text
result = {}
# Create a dictionary where we put the answer
result2 = {} 

# do a word count
for i in s.split(): 
    # if there is no word, then value = 0 otherwise add +1
    result[i] = result.get(i, 0) + 1 
    
# find out the maximal value of the repeating     
maximum = max(result.values()) 
for i, j in result.items(): 
    # the loop compares the values from result1 with the found maximum
    if j == maximum:    
        # the key and the maximum value are transferred to the new dictionary
        result2[i] = j   
# since there are 2 keys with value 12 in result2, we print the minimum key according to the condition
print(min(result2))  