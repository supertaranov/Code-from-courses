# The teacher checks the homework in class and received the following answers: 
# from n students have 
# m students had their homework eaten by a dog, and 
# k had a blackout, and 
# p students suffered both misfortunes. 
# Write a program that determines how many people did their homework.

# The format of the input data:
# The program inputs the numbers n,m,k,p, each on a separate line.

# Output data format:
# The program should print the number of students who have done their homework.

n, m, k, p = int(input()), int(input()), int(input()), int(input())
print(n-(m+k-p))   