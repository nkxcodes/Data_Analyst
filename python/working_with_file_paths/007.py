"""
Q7. — Application
You are building a Python project with this structure:
my_project/
├── main.py
├── data/
├── output/
└── backup/
Write a small program that checks whether all three folders exist:
●​ data
●​ output
●​ backup
If one of them does not exist, create it.
"""

from pathlib import Path

base_folder = Path('my_project')
data_path = base_folder / 'data'
output_path = base_folder / 'output'
backup_path = base_folder / 'backup'

if not data_path.exists():
    data_path.mkdir()

if not output_path.exists():
    output_path.mkdir()

if not backup_path.exists():
    backup_path.mkdir()