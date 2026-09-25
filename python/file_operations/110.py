"""
Q10. — Tricky
Predict what happens to the contents of data.txt after this code runs:
with open("data.txt", "w") as file:
file.write("Hello")
with open("data.txt", "w") as file:
file.write("Python")
Will the final file contain:
HelloPython
or only:
Python
Explain why.
"""

with open('data.txt', 'w') as file:
    file.write('Hello')

with open('data.txt', 'w') as file:
    file.write('Python')

"""
It only contains Python because 'w' write deletes
the old content and then add new content but if we
want to add new content with old content then we have
to use 'a' add
"""