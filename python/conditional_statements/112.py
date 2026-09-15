"""
Q12.​
Consider this program:
marks = 85if marks >= 50:
print("Pass")
if marks >= 75:
print("Good")
if marks >= 90:
print("Excellent")
Predict what it will print.
Then think about this question:
If you wanted only one final grade/message to be printed, would this structure be
appropriate? Why or why not?
"""

marks = 85

if marks >= 90:
    print("Pass")
elif marks >= 75:
    print("Good")
elif marks >= 50:
    print("Excellent")