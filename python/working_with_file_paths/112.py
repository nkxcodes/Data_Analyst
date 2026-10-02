"""
Q12. — Tricky
Consider this code:
from pathlib import Path
path = Path("students.csv")
print(path.is_file())
print(path.is_dir())
Predict what these two checks are designed to tell you.
"""

from pathlib import Path

path = Path('students.csv')

print(path.is_file()) # is_file() method is used to check whether path is a file or not.
print(path.is_dir()) # is_dir() method is used to check whether path is a folder or not.