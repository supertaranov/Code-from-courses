# The program inputs a string containing identifier strings. 
# Write a program that fixes them so that the resulting string contains no duplicates. 
# To do this, add the postfix _n to the repeated identifiers, 
# where n is the number of times such an identifier has already occurred.

# Input data format:
# At the input of the program you get a line of text, containing strings of identifiers, 
# separated by a space character.

# Output format:
# The program should output a corrected string, without duplicates and in the original order.


s = input().split()
result = {}
for i in s:
    # If the item occurs for the first time, it will be 0. If it occurs for the second time, it will be 1.
    result[i] = result.get(i, -1)+1
    # result[i] is the meaning of the dictionary
    if result[i]==0:
        # i is a dictionary key
        print(i, end=" ")
    # If it occurs a second time, the dictionary will show value 1. Print it together with the key
    elif result[i]>0:
        print(i+"_"+str(result[i]), end=" ")