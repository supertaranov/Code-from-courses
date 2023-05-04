# The variable city_name contains the name of the city (for example, Moscow), 
# and the variable city_year contains the year of its foundation (for example, 1147), 
# Fill in the missing line so that the variable city contains a tuple of the values 
# of these two variables (first the name of the city, then the year of its foundation).

city_name = input()
city_year = int(input())
city = city_name , city_year
print(city)