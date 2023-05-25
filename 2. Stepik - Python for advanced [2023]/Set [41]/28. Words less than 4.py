# Using the set generator, augment the given code to get a set containing unique words of the sentence 
# string that are less than 4 characters long. 
# Output the result on one line (lowercase) in alphabetical order, separating elements with one space character.

# Note. Note that punctuation marks do not apply to words.

sentence = '''
My very photogenic mother died in a freak accident (picnic, lightning) when I was three, 
and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows 
and dells of memory, over which, if you can still stand my style (I am writing under observation), 
the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, 
about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, 
in the summer dusk; a furry warmth, golden midges.
'''
print(*sorted(set(word.lower().strip(':,.!?();') for word in sentence.split() if len(word.strip('()!?/.,:;'))<4)))