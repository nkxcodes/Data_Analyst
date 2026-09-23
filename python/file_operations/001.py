"""
Q1. — Easy
Create a file called hello.txt and write:
Hello, Python!
into it.
Then open the file again and display its contents.
"""

with open('hello.txt', 'w') as file:
    file.write('Hello, Python!')

with open('hello.txt', 'r') as file:
    text = file.read()
    print(text)