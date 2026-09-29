"""
Q6. — Medium
Suppose you have:
base_folder = Path("Python")
Create paths for these files inside that folder:
●​ notes.txt
●​ practice.py
●​ students.csv
Use the same base_folder variable instead of repeatedly writing "Python".
"""

from pathlib import Path

base_folder = Path('Python')
path = base_folder / 'notes.txt'
path_2 = base_folder / 'practice.py'
path_3 = base_folder / 'students.csv'

print(path)
print(path_2)
print(path_3)