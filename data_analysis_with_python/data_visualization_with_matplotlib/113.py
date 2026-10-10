"""
Q13. — Mixed
You have a Python list containing daily expenses:
expenses = [120, 80, 150, 60, 200, 90, 170]
Use Python to:
1.​ Calculate the total expense.
2.​ Find the average expense.
3.​ Create a visualization showing the expenses for each day.
4.​ Clearly identify the average expense on the graph.
Use variables and Matplotlib together.
"""

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
expenses = [120, 80, 150, 60, 200, 90, 170]

total_expenses = sum(expenses)
average_expense = total_expenses / len(expenses)

plt.bar(days, expenses)
plt.xlabel('Days')
plt.ylabel('Expenses')
plt.title('Expenses')
plt.axhline(y=average_expense, label='Average Expense')

plt.legend()
plt.show()