"""
Q13.​
Create a function that receives a dictionary containing student names and marks.
The function should return the number of students who scored 50 or higher.
Use a loop and a condition inside the function.
"""

def student_scored_50_higher(u_dictionary):
    count = 0
    for marks in u_dictionary.values():
        if marks >= 50:
            count += 1
    return count

result = student_scored_50_higher({
    "Rahul": 85,
    "Aman": 92,
    "Priya": 78,
    "Manav": 45,
    "Somya": 56
})

print(result)