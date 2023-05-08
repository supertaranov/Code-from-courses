# Complete the above code so that the variable new_tuples, 
# contains a tuples list based on the tuples list with the last element 
# of each tuple replaced by a numeric value 100.

tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [i[:-1] + (100,) for i in tuples]
print(new_tuples)