# Programmer Timur wrote a program to work with biographical data of Russian poets. 
# The data are contained in tuples of the form (last name, year of birth, city of birth). 
# While the program is running, an error is found in some tuple poet_data: 
# ('Pushkin', 1799, 'Saint Petersburg'), the place of birth is wrong, 
# because Alexander Pushkin was born in Moscow.

# Supplement the above code so that the poet_data variable contains
# the correct tuple (with the corrected value), and then print its contents.

poet_data = ('Pushkin', 1799, 'Saint Petersburg')[:-1] + ('Moscow',)
print(poet_data)