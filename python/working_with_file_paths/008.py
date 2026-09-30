"""
Q8. — Application
A folder called documents contains many files.
Your program needs to find only .txt files inside that folder.
Create a program that displays the names of all .txt files it finds.
"""

from pathlib import Path

folder = Path('documents')

# .iterdir() function is use to see inside a folder.
for file in folder .iterdir():
    if file.suffix == '.txt':
        print(file)