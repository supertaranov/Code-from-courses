# The program is given one word written in lower case. Write a program that determines whether it is a palindrome.

# Input data format:
# The program receives one word in lower case as input.

# Output format:
# The program should output "YES" if the word is a palindrome and "NO" otherwise.

# Note. A palindrome is a word that reads the same in both directions. For example, the word "flood" is a palindrome.

text = input()
if text[::] == text[::-1]:
    print('YES')
else:
    print('NO')