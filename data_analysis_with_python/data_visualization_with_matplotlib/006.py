"""
Q6. — Medium
Create a graph containing two lines:
months = [1, 2, 3, 4, 5]
sales_a = [100, 120, 150, 170, 200]
sales_b = [90, 130, 140, 180, 190]
Make it possible to clearly distinguish between the two lines.
Add a title, axis labels, and a legend.
"""

import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
sales_a = [100, 120, 150, 170, 200]
sales_b = [90, 130, 140, 180, 190]

plt.plot(months, sales_a, label='Sales_A')
plt.plot(months, sales_b, label='Sales_B')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Sales Visualization')
plt.legend()
plt.show()