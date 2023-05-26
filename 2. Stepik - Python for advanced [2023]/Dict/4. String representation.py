# Write a program that will turn a natural number into a string by replacing all the digits in the number with words:
# 0 to zero;
# 1 to one;
# 2 to two;
# 3 into three;
# 4 to four;
# 5 to five;
# 6 to six;
# 7 to seven;
# 8 to eight;
# 9 by nine.

#Input data format:
# The input to the program is a natural number.

# Output data format
# The program should output a string representation of the number.

# Note. Use a dictionary instead of a conditional operator.

dict1 = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
str1 = input()
for k in str1:
    if k in dict1:
        print(dict1[k], end = ' ')