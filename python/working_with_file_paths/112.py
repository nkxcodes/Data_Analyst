"""
Q12. — Tricky
Consider this code:
from pathlib import Path
path = Path("students.csv")
print(path.is_file())
print(path.is_dir())
Predict what these two checks are designed to tell you.
Then think about this question:
Can a path exist but still not be a file?
Give an example of what that could mean.
"""

from pathlib import Path

path = Path('students.csv')

print(path.is_file()) # is_file() method is used to check whether path is a file or not.
print(path.is_dir()) # is_dir() method is used to check whether path is a folder or not.


"""
yes, path can exist but still not be a file.
For example, Path('data') can represent an existing
folder. In that case, exists() is True, but is_file()
is False.
"""

path_02 = Path('data')