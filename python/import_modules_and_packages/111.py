"""
Q11. — Tricky
A beginner writes:
import math
print(math.pi())
Find the mistake.
Think carefully about the difference between something you call like a function and a value
stored inside a module.
"""

import math

print(math.pi)

# pi is not a function which return a value but it is a variable in which value is stored.