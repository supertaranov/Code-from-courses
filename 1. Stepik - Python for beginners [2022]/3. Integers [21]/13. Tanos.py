# The mad titan Thanos has collected all 6 infinity stones and intends to wipe out 
# half the population of the universe at the snap of his fingers. 
# If the population of the universe is an odd number, 
# the titan will show mercy and round up the number of survivors. 
# Help the Avengers count the number of survivors.

# Input format:
# The input is an integer n - the population of the universe.

# Output data format:
# The program should output a single number - the number of survivors.

n = int(input())
print((n+1) // 2)