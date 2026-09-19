"""
Q15. — Challenge
You are building a small Student Utility Program.
Create a project containing:
●​
●​
●​
●​
a main Python file
your own module for student-related functions
at least two functions inside that module
the main file importing and using those functions
Your program should be able to do something useful with a student's data, such as calculating
an average, checking a result, or finding useful information from a list of marks.
Decide yourself how to divide the code between the main program and your module.
"""

from student_utils import calculate_average, check_result

average = calculate_average([45, 67, 87, 98, 45, 65, 76, 87])
result = check_result(78)

print(average)
print(result)