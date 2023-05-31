# You have access to a list of pets that contains information about dogs and their owners.  
# Each item in the list is a tuple of a kind (dog's name, owner's name, owner's last name, owner's age).

# Complete the above code so that the variable result stores a dictionary that lists each owner's dogs. 
# The key of the dictionary should be a tuple (owner's first name, last name, age), 
# and the value should be a list of dog names (keeping the original order).

# Note 1. Don't forget: tuples are immutable, so they can be dictionary keys.
# Note 2. Note that some owners have multiple dogs each.
# Note 3. There is no need to output the contents of the dictionary.

pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for pet in pets:
    # The setdefault method takes a tuple and creates a key in the dictionary from element 2 to the last
    # It also takes the 1st element from the tuple and puts it into the value
    result.setdefault(pet[1:], []).append(pet[0]) 