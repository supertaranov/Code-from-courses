# Complete the above code 
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0

# so that it outputs a single number: the sum of all the numbers in the list1 
# divided by the total number of all the numbers.

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0

for i in list1:
  counter += len(i)
  total += sum(i)
  
print(total / counter)