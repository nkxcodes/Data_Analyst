"""
Q4. — Medium
Using the os module, create a new folder called:
practice_folder
Then check whether the folder exists.
Your program should avoid trying to create it again if it already exists.
"""

import os

os.mkdir('practice_folder')
os.path.exists('practice_folder')