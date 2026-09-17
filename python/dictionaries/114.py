"""
Q14.​
You have a list of words:
["apple", "banana", "apple", "orange", "banana", "apple"]
Create a dictionary that stores each word as a key and its number of occurrences as the value.
Use a loop to build the dictionary rather than manually creating it.
"""

words = ["apple", "banana", "apple", "orange", "banana", "apple"]


fruits = {}

for word in words:
    if word in fruits:
        fruits[word] += 1
    else:
        fruits[word] = 1

print(fruits)