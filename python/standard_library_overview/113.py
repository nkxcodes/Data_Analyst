"""
Q13. — Mixed
You have:
students = [
{"name": "Rahul", "marks": 78},
{"name": "Aman", "marks": 91},
{"name": "Priya", "marks": 65}
]
Create a program that:
1.​ Saves the student data into a JSON file.
2.​ Reads the data back from the file.
3.​ Uses a loop to display each student's name and marks.
This combines dictionaries, lists, loops, JSON, and file handling.
"""

import json

students = [
{"name": "Rahul", "marks": 78},
{"name": "Aman", "marks": 91},
{"name": "Priya", "marks": 65}
]

with open('students.json', 'w') as file:
    json.dump(students, file)

with open('students.json', 'r') as file:
    data = json.load(file)

    for row in data:
        print(f'{row["name"]}: {row["marks"]}')