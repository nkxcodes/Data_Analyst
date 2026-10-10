"""
Q13. — Mixed
You are given:
expenses = pd.DataFrame({ "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
"amount": [120, 80, 150, 60, 200, 90, 170]})
Using Python and Seaborn:
calculate the total and average expense
visualize daily expenses
make the average expense visible on the graph
give the graph a title and meaningful labels
Your visualization should make it easy to identify days when expenses were unusually high.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

expenses = pd.DataFrame({ "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
"amount": [120, 80, 150, 60, 200, 90, 170]})

total_expenses = sum(expenses['amount'])
average_expense = total_expenses / len(expenses['amount'])

sns.lineplot(x='day', y='amount', data=expenses, marker='o')
plt.axhline(y=average_expense, color='red',label=f'Average: {average_expense:.2f}')
plt.xlabel('Days')
plt.ylabel('Expense Amount (₹)')
plt.title('Daily Expenses Throughout the Week')

plt.legend()
plt.show()