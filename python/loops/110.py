"""
Q10.​
Predict what the following program will do before running it:
for i in range(5):
print(i)
What numbers will be printed?
Then change it to print numbers from 1 to 5.
Finally, explain why range(5) does not produce 5.
"""

for i in range(5):
    print(i)

# Prints - 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)

# range(5) does not produced 5 because stop or second number is excluded in range