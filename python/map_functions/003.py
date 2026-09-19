"""
Q3. — Easy
You have:
names = ["rahul", "aman", "priya", "neha"]
Use map() to convert every name into uppercase.
"""

names = ['rahul', 'aman', 'priya', 'neha']

result = map(lambda name: name.upper(), names)

print(list(result))