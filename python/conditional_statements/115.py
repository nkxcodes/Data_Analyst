"""
Q15.​
Create a small student result checker.
The program should take a student's name and marks in three subjects.
Determine whether the student passes or fails based on these rules:
●​ The student must score at least 33 in each subject.
●​ The average marks must be at least 40.
If the student passes, display a suitable result containing their name. Otherwise, display that
they failed.
Decide yourself how to organize the variables and conditions.
"""

student_name = input('Enter student name: ')
subject_1 = float(input('Enter subject 1 marks: '))
subject_2 = float(input('Enter subject 2 marks: '))
subject_3 = float(input('Enter subject 3 marks: '))

total_marks = subject_1 + subject_2 + subject_3
average = total_marks / 3

if (subject_1 >= 33 and
    subject_2 >= 33 and
    subject_3 >= 33) and average >= 40:
    print()
    print(student_name)
    print('Passed')
else:
    print('Failed!')