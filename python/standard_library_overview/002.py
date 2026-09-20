"""
Q2. — Easy
Import the os module.
Write a small program that displays:
1.​ The current working directory.
2.​ The names of the files and folders inside the current directory.
"""

import os 

current_working_directory = os.getcwd()
print(current_working_directory)

print(os.listdir())