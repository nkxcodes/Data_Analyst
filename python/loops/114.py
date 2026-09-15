"""
Q14.​
Create a program that takes a word from the user and examines each character.
Count how many characters are:
●​ vowels
●​ consonants
Assume the user enters a simple word containing only alphabetic characters.
"""

u_string = input('Enter a word: ')
vowels = 0
consonants = 0

for ch in u_string:
    if ch in ['a', 'e', 'i', 'o', 'u'
              'A', 'E', 'I', 'O', 'U']:
        vowels += 1
    else:
        consonants += 1

print(f'Vowels: {vowels}')
print(f'Consonants: {consonants}')