"""
Q9. — Application
Create a small program that asks the user for a filename and then tries to read it.
The program should:
1.​ Try to open the file.
2.​ If opening fails, display an appropriate error message.
3.​ If opening succeeds, process the file.
4.​ Perform some action that should happen regardless of whether an error occurred.
Use the appropriate exception-handling blocks to organize these steps.
"""

try:
    file_name = input('Enter file name: ')
    with open(file_name, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('File not found!')
else:
    print(content)
finally:
    print('Execution completed!')