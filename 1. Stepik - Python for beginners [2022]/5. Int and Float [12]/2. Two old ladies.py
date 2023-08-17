# Two old ladies are walking towards each other with constant speeds V1 and V2 km/h. 
# Determine in what time the two old ladies will meet if the distance between them is S km.

# Input data format:
# You are given three floating point numbers S, V1, V2, each on a separate line.

# Output data format:
# The program has to print out one number according to the problem.

# Note. These are very fast old ladies.

s, v1, v2 = float(input()), float(input()), float(input())
print(s / (v1 + v2))