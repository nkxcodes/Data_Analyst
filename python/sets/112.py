"""
Q12.​
Predict the result of each operation before running the program:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)
print(A & B)
print(A - B)
print(A ^ B)
Then explain in your own words what each of the four operations represents.
"""

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B) # {1, 2, 3, 4, 5, 6} - Combine everything from both sets
print(A & B) # {3, 4} - Common elements in a and b.
print(A - B) # {1, 2} - What A has but B does not have.
print(A ^ B) # {1, 2, 5, 6} Elements that are not common in both.

# The python function for this (^) is symmetric_difference().