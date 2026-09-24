"""
Q5. — Medium
Create a file called log.txt.
Write one message to it.
Then open the same file again and add another message without deleting the first message.
Repeat this with a third message.
Your final file should contain all three messages.
"""

with open('log.txt', 'w') as file:
    file.write('Hello!')

with open('log.txt', 'a') as file:
    file.write('\nHow Are You?')

with open('log.txt', 'a') as file:
    file.write('\nMy Friend.')