"""
Q14. — Mixed
A folder contains several files:
report.txt
data.csv
photo.jpg
students.csv
notes.txt
image.png
Create a program that:
1.​ Finds the .csv files.
2.​ Creates a folder called csv_backup.
3.​ Copies all CSV files into that folder.
4.​ Displays how many CSV files were copied.
Use the appropriate standard-library modules rather than manually copying the files.
"""

import shutil, os

files = os.listdir()

os.mkdir('csv_backup')

count = 0
for file in files:
    if file.endswith('.csv'):
        shutil.copy(file, 'csv_backup/')
        count += 1


if count >= 2:
    print(f'{count} CSV files copied')
else:
    print(f'{count} CSV file copied')