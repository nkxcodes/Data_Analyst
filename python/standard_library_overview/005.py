"""
Q5. — Medium
Using shutil, create a small program that:
1.​ Creates a file called notes.txt.
2.​ Creates a folder called backup.
3.​ Copies notes.txt into the backup folder.
4.​ Verify that the copied file exists.
Think about why shutil is useful here instead of manually reading and rewriting the file.
"""

import shutil
import os


file = open('notes.txt', 'w')
file.close()

os.mkdir('backup')

shutil.copy('notes.txt', 'backup/')

os.path.exists('backup/notes.txt')