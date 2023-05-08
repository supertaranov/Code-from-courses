# Complete the above code to get a list that contains only non-empty tuples 
# from the original tuples list, without changing the order of the tuples.

tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if len(i) > 0]
print(non_empty_tuples)