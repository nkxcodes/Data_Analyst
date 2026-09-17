"""
Q6.​
Create a dictionary containing several key-value pairs.
Practice:
●​
●​
●​
●​
checking whether a particular key exists,
safely retrieving a value when a key may not exist,
removing an entry,
clearing the entire dictionary.
Do these operations separately so you can observe what each one does.
"""

students = {
    "Rahul": 85,
    "Aman": 92,
    "Priya": 78,
    "Manav": 45,
    "Somya": 56
}

# whether a particular key exists.
print('Rahul' in students)
print('Aditya' in students)

# safely retrieving a value when a key may not exist.
# get() is used for safely retrieving a value when key may not exists.
print(students.get('Vansh', 'Student not found.'))

# remove an entry.
result = students.pop('Rahul')

# clearing the entire dictionary.
students.clear()

print(students)