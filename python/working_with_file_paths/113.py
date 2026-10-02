"""
Q13. — Mixed
You have a folder called numbers.
Inside it are several .txt files.
Create a program that:
1.​ Finds all .txt files.
2.​ Opens each file.
3.​ Reads the numbers inside.
4.​ Calculates the total of the numbers in each file.
5.​ Displays the file name and its total.
Combine paths, file operations, loops, lists, and numbers.
"""

from pathlib import Path

base_folder = Path('numbers')

total = 0
for file in base_folder.iterdir():
    with open(f'{file}', 'r') as opened_file:
        content = opened_file.read()
        content = content.split()
        numbers = []

        for number in content:
            numbers.append(int(number))

        for number in numbers:
            total += number

        print(f'{file.name}: {total}')
        total = 0