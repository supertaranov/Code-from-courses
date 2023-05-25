# The satellite carries a device for measuring solar activity. 
# Every minute it transmits a positive integer number - 
# the amount of solar radiation energy - 
# to the observatory via the communication channel. 
# There is no need to keep repeating data for proper analysis of the results. 
# Write a program that outputs the maximum number of satellite readings that, when removed, 
# will correctly analyze the result.

# Input Data Format:
# The program inputs a single line containing numbers - the readings of the Voskhod satellite. 
# The numbers are space-separated and contain no leading zeros.

# Output data format:
# The program should output the maximum number of readings, 
# after deleting which the analysis of results will be correct.

list1 = [i for i in input().split()]
print(len(list1)-len(set(list1)))