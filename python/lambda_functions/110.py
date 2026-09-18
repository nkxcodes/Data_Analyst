"""
Q10. — Tricky
Predict what this code does before running it:
double = lambda x: x * 2
print(double)
print(double(5))
Explain why the two print() statements produce different kinds of output.
"""

double = lambda x: x * 2

print(double) # double refers to the function itself.
print(double(5)) # calls the function with 5 and gets the returned result.