"""
Q11.​
Find and fix the mistake in this program:
age = 18
if age >= 18
print("Adult")
else:
print("Minor")
After fixing it, explain why Python could not understand the original condition.
"""

age = 18

if age >= 18: # - this colon is not there
    print("Adult")
else:
    print("Minor")