"""
Q9. — Application
A file called notes.txt contains many lines.
You want to create another file called python_notes.txt containing only the lines that
contain the word "Python".
Create a program that performs this task.
"""

with open('notes.txt', 'r') as file:
    reader = file.read()
    reader = reader.split('\n')

    for line in reader:
        if 'Python' in line:
            with open('python_notes.txt', 'a') as file:
                file.write(f'\n{line}')