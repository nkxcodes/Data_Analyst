"""
Q8. — Application
A program needs to know what files are inside a folder.
Using os, create a program that displays only files ending in:
.txt
Do not display other file types or folders.
"""

import os

files = os.listdir()

for file in files:
    if file.endswith('.txt'):
        print(file)