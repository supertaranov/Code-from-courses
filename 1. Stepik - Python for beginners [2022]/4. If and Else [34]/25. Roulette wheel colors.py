# On the roulette wheel, the pockets are numbered from 0 to 36. 
# The following are the colors of the pockets: 

# pocket 0 is green;
# for pockets 1 to 10, odd-numbered pockets are red, even-numbered pockets are black;
# for pockets 11 to 18, the odd-numbered pockets are black, the even-numbered pockets are red;
# for pockets 19 to 28, the odd-numbered pockets are red, the even-numbered pockets are black;
# for pockets 29 to 36, odd-numbered pockets are black, even-numbered pockets are red.
# Write a program that reads the pocket number and shows whether that pocket is green, red, or black. 
# The program should print an error message if the user enters a number that lies outside the range 0 to 36.

# Input data format:
# The program inputs a single integer number.

# Output data format:
# The program should output the color of the pocket, or the "input error" message 
# if the entered number lies outside the 0 to 36 range.

a = int(input())
if 0<=a<37:
  if (0<a<11 or 18<a<29) and a%2 or (10<a<19 or 28<a<37) and a%2==0:
    print('red')
  elif a == 0:
    print('green')
  else:
    print('black')
else:
  print('input error')