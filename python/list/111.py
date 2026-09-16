"""
Q11.​
Find and fix the mistake in this program:
fruits = ["apple", "banana", "mango"]
fruits[3] = "orange"
print(fruits)
The programmer wants orange to become the fourth item in the list.
After fixing it, explain why the original code causes a problem.
"""

fruits = ['apple', 'banana', 'mango']
# fruits[3] = "orange"

fruits.append('orange')

print(fruits)

# Index three did not even exist in this list