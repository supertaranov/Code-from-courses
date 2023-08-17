# The names of three cities are given. 
# Write a program that determines the shortest and the longest city name.

# Input data format:
# The program inputs the names of three cities, each on a separate line.

# Output data format:
# The program should output the shortest and longest city name, each on a separate line.

# Note. It is guaranteed that the lengths of all three city names are different.

city1, city2, city3 = input(), input(), input()
a = len(city1)
b = len(city2)
c = len(city3)
if a < b < c:
    print(city1)
    print(city3)
elif a < c < b:
    print(city1)
    print(city2)
elif b < c < a:
    print(city2)
    print(city1)
elif b < a < b:
    print(city2)
    print(city3)
elif c < a < b:
    print(city3)
    print(city2)
elif c < b < a:
    print(city3)
    print(city1)