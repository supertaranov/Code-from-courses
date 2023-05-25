# During the summer break, Timur and the students of the BEEGEEK online school 
# decided to take a vacation. As a result: 
# n students of the school went on vacation to the sea, 
# m students went to the countryside, and 
# k students went to the mountains. 
# It turned out that both in the village and at the sea there were x students, 
# and in the village and in the mountains - y students. 
# No one managed to visit both the mountains and the sea. 

# Write a program to determine the number of students in the school if no one was able 
# to visit all three places at once, and z students were taking math exams for admission 
# to Moscow State University, and they didn't go anywhere.

# Input data format:
# The input to the program is the numbers 
# n,m,k,x,y,z, each on a separate line.

# Output data format:
# The program should output one number according to the problem's condition.

n,m,k,x,y,z = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
total = (n+m+k-x-y) + z
print(total)