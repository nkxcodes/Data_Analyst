"""
Q6. — Medium
Understand the difference between these file modes:
●​ r
●​ w
●​ a
For each mode, create a small experiment that shows what happens when you use it on an
existing file.
Pay particular attention to what happens to the old content when using w.
"""

with open('story.txt', 'r') as file:
    reader = file.read()
    print(reader)

with open('story.txt', 'w') as file:
    file.write('Hello!')

with open('story.txt', 'a') as file:
    file.write('\nHow Are You?')