# Using the set generator, augment the above code to get a set containing unique values of the items list. 
# Output the result on a single line, in ordered form, separating items with one space character.

# Note 1. Note that some list items are numbers and some are strings, and strings should be treated as numbers.

items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
set1 = set(int(i) for i in items)
print(*sorted(set1))