"""
Q8.
A student has marks in three subjects.
Create a function that receives the three marks and returns the student's average.
Then, outside the function, use the returned average to determine whether the student passed
or failed.
"""

def calculate_average(sub_1, sub_2, sub_3):
    return (sub_1 + sub_2 + sub_3) / 3

average = calculate_average(23, 43, 46)

if average >= 33:
    print('Passed.')
else:
    print('Failed.')