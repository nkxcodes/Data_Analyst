"""
Q12.​
Consider this dictionary:
data = {
"name": "Nitesh",
"age": 18,
"marks": [80, 75, 90]
}
Answer these questions by working with the dictionary:
1.​ How would you access the list of marks?
2.​ How would you access the first mark inside that list?
3.​ How would you change the second mark to 85?
This question is about understanding how different Python data structures can exist inside a
dictionary.
"""

data = {
    "name": "Nitesh",
    "age": 18,
    "marks": [80, 75, 90]
}

# 1.​ How would you access the list of marks?
print(data['marks'])

# 2.​ How would you access the first mark inside that list?
print(data['marks'][0])

# 3.​ How would you change the second mark to 85?
data['marks'][1] = 85
print(data)