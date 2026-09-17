"""
Q15.
Build a small student result system using functions.
The program should accept a student's:
●​ name
●​ marks in three subjects
It should calculate the total and average, determine whether the student passed, and display a
meaningful result.
Decide yourself:
what functions you need,
what each function should receive,
what each function should return,
and how the functions should work together.
The goal is not to make a large program, but to use functions naturally to break one problem
into smaller reusable pieces.
"""

import math


def calculate_total_and_average(name, sub_1, sub_2, sub_3):
    is_passed = True
    if sub_1 < 33 or sub_2 < 33 or sub_3 < 33:
        is_passed = False
    return name, sub_1 + sub_2 + sub_3, (sub_1 + sub_2 + sub_3) / 3, is_passed

name, total, average, is_passed = calculate_total_and_average('Manav', 34, 56, 76)

if is_passed:
    print(f'{name} is passed with total of {total} marks and an average of {round(average, 2)}.')
else:
    print(f'{name} unfortunately failed.')