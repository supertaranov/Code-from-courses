# Complete the above code 

# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1

# using the for loop and the built-in max() function so that it outputs 
# one common maximum element among all the elements of the nested list1 lists.

list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1
for i in list1:
    if max(i) > maximum:
        maximum = max(i)
print(maximum)