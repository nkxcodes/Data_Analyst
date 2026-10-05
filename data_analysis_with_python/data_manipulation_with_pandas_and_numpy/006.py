"""
Q6. — Medium
Given:
df = pd.DataFrame({
"department": ["IT", "HR", "IT", "Sales", "HR", "IT"],
"salary": [25000, 30000, 28000, 35000, 32000, 27000]
})
Group the employees by department.
For each department, find the average salary.
Then find the number of employees in each department.
"""

import pandas as pd

df = pd.DataFrame({
"department": ["IT", "HR", "IT", "Sales", "HR", "IT"],
"salary": [25000, 30000, 28000, 35000, 32000, 27000]
})

department_average_salary = df.groupby('department')['salary'].mean().round(2)
number_of_employees = df.groupby('department')['salary'].count()

print(f'{department_average_salary}')
print(f'{number_of_employees}')