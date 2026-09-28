"""
Q4. — Medium
You have:
project/
├── main.py
└── data/
└── students.csv
Create a path for students.csv starting from the project directory.
Then use the path to check whether the file exists.
"""

from pathlib import Path

path = Path('project') / 'data' / 'students.csv'

print(path)
print(path.exists())