"""
Q12. — Tricky
Find the mistake in this code:
with open("students.txt", "r") as file:
data = file.read()
print(file.read())
The programmer wants to read the file again after the with block.
What is wrong with this approach?
Also explain why using with open(...) is generally safer than manually opening and closing
files.
"""

with open('students.txt', 'r') as file:
    data = file.read()

print(data)

"""
With this approach, wrong is this that we opened file
but after when open block finishes, python closes the file
automatically, and then if we try to access or try to read
the file, it will give error.

Solution :- The solution is we have to store the readings
of file inside variable and then we access it's content
anywhere in the file.
""" 

"""
open() generally safer because without open() we have
to remeber to close() the file using file.close().

and if something goes wrong before file.close(),
the file might remain open.
"""