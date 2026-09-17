"""
Q15.​
Imagine you are building a small course registration system.
There are two courses, each containing a collection of registered students.
Your program should determine:
1. students registered in both courses,
2. students registered only in the first course,
3. students registered only in the second course,
and the total number of unique students registered across both courses.
Decide yourself how sets can naturally represent this situation and how you will organize the
program.
"""

course_1 = ["Rahul", "Aman", "Priya", "Neha", "Rohan", "Karan"]
course_2 = ["Priya", "Neha", "Vikas", "Simran", "Rohan", "Arjun"]

course_1 = set(course_1)
course_2 = set(course_2)

# 1. students registered in both courses - intersection for common elements
print(course_1.intersection(course_2))

# 2. students registered only in the first course - difference
print(course_1.difference(course_2))

# 3. students registered only in the second course - difference
print(course_2.difference(course_1))

# 4. total number of unique students registered across both courses.
print(len(course_1 | course_2))