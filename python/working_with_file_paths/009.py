"""
Q9. — Application
You have a folder called images.
You want to count how many files inside it have these extensions:
●​ .jpg
●​ .png
●​ .jpeg
Create a program that checks the files and displays the total number of image files.
"""

from pathlib import Path

folder = Path('images')

count = 0
for file in folder.iterdir():
    if file.suffix in ('.jpg', '.png', '.jpeg'):
        count += 1

print(f'Total number of image files are {count}')