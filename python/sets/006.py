"""
Q6.​
Using the same two sets from Q5, find:
●​ all elements that belong to either set,
●​ elements that belong to Set A but not Set B,
●​ elements that belong to Set B but not Set A.
Think about how these operations are different from simply checking membership.
"""

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# ●​ all elements that belong to either set - (|)(union) - combine both sets
print(set_a.union(set_b))
print(set_a | set_b)