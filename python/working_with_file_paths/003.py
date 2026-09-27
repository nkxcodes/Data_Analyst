"""
Q3. — Easy
Create a Path object for a folder called:
Python
Then create another path representing:
Python/notes.txt
Do this using pathlib rather than manually writing the entire path as one string.
"""

from pathlib import Path

folder = Path('Python')
file_name = 'notes.txt'

path = folder / file_name

print(path)