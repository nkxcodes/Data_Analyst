"""
Q10.​
Predict what the following program will print before running it:
student = {
"name": "Nitesh",
"age": 18
}
student["age"] = 19
student["city"] = "Delhi"
print(student)
Then explain why "age" changes while "city" is added.
"""

student = {
    "name": "Nitesh",
    "age": 18
}

student["age"] = 19 # age is already there in dictionary, that's why it changes
student["city"] = 'Delhi' # city is not in dictionary, that's why it created new key value pair

print(student)