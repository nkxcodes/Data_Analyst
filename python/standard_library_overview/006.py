"""
Q6. — Medium
You have this Python dictionary:
student = {
"name": "Rahul",
"age": 17,
"marks": [78, 85, 91]
}
Use json to:
1.​ Convert the dictionary into JSON data.
2.​ Convert that JSON data back into a Python object.
Observe the difference between the Python dictionary and its JSON representation.
"""

import json

student = {
"name": "Rahul",
"age": 17,
"marks": [78, 85, 91]
}

with open('student.json', 'w') as file:
    json.dump(student, file)

with open('student.json', 'r') as file:
    student = json.load(file)

print(student)