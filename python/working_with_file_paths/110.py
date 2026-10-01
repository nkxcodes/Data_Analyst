"""
Q10. — Tricky
Predict what each of these paths represents:
Path("notes.txt")
Path("./notes.txt")
Path("data/notes.txt")
Path("../notes.txt")
Explain the meaning of:
●​ .
●​ ..
●​ a relative path
Do not just describe the syntax—think about where Python starts looking from.
"""

from pathlib import Path

path_01 = Path('notes.txt')
path_02 = Path('./notes.txt')
path_03 = Path('data/notes.txt')
path_04 = Path('../notes.txt')

"""
. means the current directory. It tells Python to look from
the current directory.
.. means the parent directory. It tells Python to go one
directory up from the current directory.
A relative path is a path that tells the location of a file
or folder relative to the current working directory.
"""