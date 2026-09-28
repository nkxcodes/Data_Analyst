"""
Q5. — Medium
Create a path representing:
data/students.csv
Use the path to find:
1.​ The file name.
2.​ The file extension/suffix.
3.​ The file name without its extension.
4.​ The parent folder.
"""

from pathlib import Path

path = Path('data') / 'students.csv'

print(path.name) # Prints file name.
print(path.suffix) # Prints file extension.
print(path.stem) # Prints file name without extension.
print(path.parent) # Prints file parent name.