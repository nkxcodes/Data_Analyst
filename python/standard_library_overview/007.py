"""
Q7. — Application
A school stores student information in a CSV file.
Each row contains:
Name, Age, Marks
Create a small program that creates a CSV file containing information for 5 students.
Then read the CSV file and display each student's information.
"""

import csv

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerows([
        ['Name', 'Age', 'Marks'],
        ['Manav', 17, 78],
        ['Aman', 16, 87]
    ])

with open('students.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)