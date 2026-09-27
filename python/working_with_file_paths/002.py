"""
Q2. — Easy
Create a Path object representing:
projects/python/main.py
Print:
1.​ The complete path.
2.​ The file name.
3.​ The file extension.
"""

from pathlib import Path

path = Path('projects/python/main.py')

print(path) # prints relative path.
print(path.name) # prints file name.
print(path.suffix) # prints file extension. 