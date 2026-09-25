"""
A beginner writes:
file = open("notes.txt", "r")
content = file.read()
print(content)
content = file.read()
print(content)
Why might the second print() not display the file contents again?
What concept about a file object's current position does this demonstrate?
"""

file = open('notes.txt', 'r')
content = file.read()
print(content)

content = file.read()
print(content)

"""
A file object remebers where we are currently in the file.
read() moves that position forward.
"""