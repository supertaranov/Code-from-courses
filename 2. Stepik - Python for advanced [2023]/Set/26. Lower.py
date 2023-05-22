# Using the set generator, augment the above code to get a set containing the 
# first letter of each word (lowercase) of the words list. 
# Output the result on one line in alphabetical order, separating elements with one space character.

words = [
    'Plum', 
    'Grapefruit', 
    'apple', 
    'orange', 
    'pomegranate', 
    'Cranberry', 
    'lime', 
    'Lemon', 
    'grapes', 
    'persimmon', 
    'tangerine', 
    'Watermelon', 
    'currant', 
    'Almond'
    ]
set1 = set(i[0].lower() for i in words)
print(*sorted(set1))