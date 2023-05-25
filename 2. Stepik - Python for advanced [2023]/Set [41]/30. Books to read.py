# Grade 10 students at BEEGEEK Online School were assigned three books to read over summer break:
# "What is Math?"
# "Math Composition;
# "100 Genius Math Ideas."
# It turned out that 
# n students had read the first book, 
# m students read the second book, 
# k students read the third book. It is also known that 
# x students have read the first or second or both books, 
# y students read the second or third, or both, 
# z students read the first and third, or at least one of these two books. 
# Only t students fully completed the assignment. 
# There are a total of a students in 10th grade. 

# Write a program that outputs how many students:
# have read only one book;
# have read two books;
# have not read any of the recommended books.

# Input data format:
# This program takes the following numbers as input 
# n,m,k,x,y,z,t,a, each on a separate line.

# Output data format:
# The program should output three numbers according to the problem condition, each on a separate line.

n,m,k,x,y,z,t,a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
only_first_book = n-(n+m-x-t)-(n+k-z-t)-t
only_second_book = m-(n+m-x-t)-(m+k-y-t)-t
only_third_book = k-(n+k-z-t)-(m+k-y-t)-t

one_book = only_first_book + only_second_book + only_third_book
two_books = (n+m-x-t)+(n+k-z-t)+(m+k-y-t)
no_books = a-one_book-two_books-t

print(one_book)
print(two_books)
print(no_books)