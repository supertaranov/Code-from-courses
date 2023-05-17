# Complete the above code so that it outputs the elements of the fruits set, 
# each on a separate line, sorted in descending order (in reverse lexicographic order).

# Note. Output each element of the set on a separate line.

fruits = {
    'apple',
    'banana',
    'cherry', 
    'avocado', 
    'pineapple', 
    'apricot', 
    'banana', 
    'avocado', 
    'grapefruit'
    }

print(*sorted(fruits, reverse=True), sep='\n')