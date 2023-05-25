# When the BEEGEEK Online School accepts new employees, its director tests not only the candidate's professional 
# qualities, but also his or her memory.

# The candidate is briefly shown several different numbers, and then has to name them. 
# It does not matter in what order he recalls them, and whether he repeats them or not, 
# the main thing is that he must name all the numbers, without adding extra ones.

# Write a program that determines whether the candidate has successfully passed the memory test.

# The format of the input data:
# The program inputs two lines of numbers: the first line contains the numbers shown to the candidate 
# and the second line contains the candidate's answers.

# Output format:
# The program should output YES if the candidate passed the test and can be hired and NO otherwise.

set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
print('YES' if set1==set2 else 'NO')