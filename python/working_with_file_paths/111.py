"""
Q11. — Tricky
A beginner writes:
from pathlib import Path
path = Path("data") / "students.csv"
if path.exists:
print("File exists")
Find the mistake.
Why does this condition not correctly check whether the path exists?
"""

from pathlib import Path

path = Path('data') / 'students.csv'

if path.exists():
    print('File exists')

"""
exists() is method, so for calling it we need
to use parenthesis.
but if we don't use parenthesis, then it is referring to
the method and not calling the method.

-- exists() is a method, Parentheses () are used to
call/execute the method and get it's result
"""