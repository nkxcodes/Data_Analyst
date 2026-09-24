"""
Q8. — Application
A file called marks.txt contains one mark per line:
78
91
65
84
72
Read the file and calculate:
total marks
average marks
highest mark
lowest mark
The values are stored as text in the file, so handle them appropriately.
"""

with open('marks.txt', 'r') as file:
    reader = file.read()
    reader = reader.split()

    marks = []
    for value in reader:
        marks.append(int(value))

    total_marks = 0
    for value in marks:
        total_marks += value

    average_marks = total_marks / len(reader)
    highest_marks = max(marks)
    lowest_marks = min(marks)

    print(f'Total Marks: {total_marks}')
    print(f'Average Marks: {average_marks}')
    print(f'Highest Marks: {highest_marks}')
    print(f'Lowest Marks: {lowest_marks}')