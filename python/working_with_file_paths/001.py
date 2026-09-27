"""
Q1. — Easy
Import Path from Python's pathlib module.
Create a Path object representing a file named:
notes.txt
Print the path.
"""

from pathlib import Path

path = Path('notes.txt')

print(path)