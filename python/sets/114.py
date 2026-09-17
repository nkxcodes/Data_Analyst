"""
Q14.​
You have two lists of student names:
●​ students who submitted an assignment
●​ students who attended the class
Use sets to find the students who attended but did not submit the assignment.
Display their names.
"""

submitted = ["Rahul", "Aman", "Priya", "Neha", "Rohan"]
attended = ["Rahul", "Aman", "Priya", "Neha", "Rohan", "Karan", "Simran", "Vikas"]

submitted = set(submitted)
attended = set(attended)

print(attended.difference(submitted))
print(attended - submitted)