"""
Q15. — Challenge
You are building a small Student Data Organizer.
Your program should work with a CSV file containing:
Name, Marks
It should:
1.​ Read the student records.
2.​ Find students whose marks are 75 or higher.
3.​ Save those students into a separate JSON file.
4.​ Create a backup folder and copy the original CSV file into it.
5.​ Display how long the main processing took.
Use the standard library modules you have learned where they naturally fit.
You do not need to use every module from this topic. Decide yourself which ones are
actually useful for each part.
"""

import time, csv, json, os, shutil

start = time.time()

passing_students = []

with open('students.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        marks = int(row[1])
        if marks >= 75:
            passing_students.append(row)

with open('students.json', 'w') as file:
    json.dump(passing_students, file)

os.mkdir('backup')

shutil.copy('students.csv', 'backup/')

end = time.time()
print(f'Time taken: {end - start}')