"""
Q5.​
Create two sets:
●​ Set A: numbers from 1 to 5
●​ Set B: numbers from 4 to 8
Find the elements that are present in both sets.
"""

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# intersection(&) -> common elements in both sets

print(set_a.intersection(set_b))
print(set_a & set_b)