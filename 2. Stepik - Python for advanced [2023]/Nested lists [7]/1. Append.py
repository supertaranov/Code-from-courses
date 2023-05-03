# Complete the above code 
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# using the list method append() so that the list1 list looks like:
# list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)