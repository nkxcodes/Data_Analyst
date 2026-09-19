"""
Q14. — Mixed
Imagine this folder structure:
my_project/
│
├── main.py
│
└── tools/
├── __init__.py
└── calculator.py
calculator.py contains a function called multiply().
Your task is to use multiply() inside main.py.
Write the import statement you would need and explain what tools represents in this structure.
"""

from tools.calculator import multiply

result = multiply(3, 2)

print(result)