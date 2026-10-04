"""
Q7. — Application
You have this employee data:
employees = pd.DataFrame({
"name": ["Raj", "Anita", "Vikram", "Sara"],
"salary": [25000, 32000, 28000, 40000],
"department": ["IT", "HR", "IT", "Sales"]
})
The manager wants to see only the employees who work in the IT department.
Create and print that result.
"""

import pandas as pd

employees = pd.DataFrame({
"name": ["Raj", "Anita", "Vikram", "Sara"],
"salary": [25000, 32000, 28000, 40000],
"department": ["IT", "HR", "IT", "Sales"]
})

employees_at_IT = employees[employees['department'] == 'IT']

print(employees_at_IT)