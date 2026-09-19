"""
Q3. — Easy
You have:
names = ["Aman", "Rahul", "Alexander", "Neha", "Priya"]
Use filter() to keep only the names whose length is greater than 5.
"""

names = ['Aman', 'Rahul', 'Alexander', 'Neha', 'Priya']

result = filter(lambda name: len(name) > 5, names)

print(list(result))