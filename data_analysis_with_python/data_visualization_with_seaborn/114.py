"""
Q14. — Mixed
A company records employee salaries:
employees = pd.DataFrame({ "department": ["IT", "IT", "HR", "HR", "Sales", "Sales"],
"gender": ["M", "F", "F", "M", "M", "F"], "salary": [40000, 45000, 30000, 32000, 35000, 38000]})
Create a visualization that compares salaries across departments and distinguishes employees
by gender.
Then explain what your graph allows you to compare and one thing it cannot reliably prove
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

employees = pd.DataFrame({ "department": ["IT", "IT", "HR", "HR", "Sales", "Sales"],
"gender": ["M", "F", "F", "M", "M", "F"], "salary": [40000, 45000, 30000, 32000, 35000, 38000]})

sns.barplot(x='department', y='salary', hue='gender', data=employees)
plt.title('Average Salary by Department and Gender')
plt.xlabel('Department')
plt.ylabel('Salary')

plt.show()

"""
1. What it compares: The average salaries of male and females
employees within each department.
2. What it cannot prove: It cannot prove that gender causes
salary differences or that any differences are unfair,
especially because the dataset contains only six employees.
"""