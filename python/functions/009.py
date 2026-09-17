"""
Q9.
Create a function that receives a word and determines whether it is a palindrome.
For example, a palindrome reads the same forwards and backwards.
The function should return a Boolean value rather than directly printing the answer.
"""

def is_palindrome(word):
    return word == word[::-1]

result = is_palindrome('MOM')

print(result)