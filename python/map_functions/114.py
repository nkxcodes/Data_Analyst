"""
Q14. — Mixed
You have:
names = ["Rahul", "Alexander", "Aman", "Priya", "Christopher"]
Use map() to create a result containing the length of each name.
Then, using a concept you learned earlier, determine the longest name from those
lengths/names.
"""

names = ['Rahul', 'Alexander', 'Aman', 'Priya', 'Christopher']

result = map(lambda name: len(name), names)

lengths = list(result)

print(lengths)

for name in names:
    if len(name) == max(lengths):
        print(name)