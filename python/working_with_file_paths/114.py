"""
Q14. — Mixed
You have this folder:
project/
├── main.py
├── notes.txt
├── students.csv
├── data.json
├── image.png
└── README.md
Create a program that examines the files and groups their paths into categories:
Python files
Text/Markdown files
Data files (.csv, .json)
Image files
Use the file paths to determine which category each file belongs to.
"""

from pathlib import Path

python_files = []
text_files = []
data_files = []
image_files = []

base_folder = Path('project')

for file in base_folder.iterdir():
    if file.suffix == '.py':
        python_files.append(file)
    elif file.suffix in ('.txt', '.md'):
        text_files.append(file)
    elif file.suffix in ('.csv', '.json'):
        data_files.append(file)
    elif file.suffix in ('.png', '.jpg', '.jpeg'):
        image_files.append(file)

print(f'Python Files: {python_files}')
print(f'Text Files: {text_files}')
print(f'Data Files: {data_files}')
print(f'Image Files: {image_files}')