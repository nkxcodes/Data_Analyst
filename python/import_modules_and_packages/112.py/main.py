"""
Q12. — Tricky
Suppose you create a file called:
calculator.py
Inside it you define a function called add().
Now create another Python file called:
main.py
Your goal is to use add() from calculator.py inside main.py.
Describe what you need to do so that main.py can use the function.
Then explain what a module means in this situation.
"""

from calculator import add

result = add(2, 3)

print(result)