"""
Q11.​
Find and fix the mistake in this code:
student = ("Nitesh", 18, "Delhi")
name, age = student
print(name)
print(age)
The programmer wants to store all the information from the tuple in separate variables.
After fixing it, explain why the original code doesn't work.
"""

student = ('Nitesh', 18, 'Delhi')
name, age, city = student

print(name)
print(age)

# tuple contains three elements but we assinging values over two variables only