"""
Q5. — Medium
A shop records its daily sales:
sales = pd.DataFrame({ "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
1500, 1100, 1800, 2000, 2500]})
"sales": [1200,
Create a Seaborn line plot to visualize the sales trend.
Customize the plot so the individual observations are visible along with the line.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sales = pd.DataFrame({
    "day": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
    "sales": [1200, 1500, 1100, 1800, 2000, 2500]
})

sns.lineplot(x='day', y='sales', data=sales, marker='o')
plt.title('Daily Sales Trend')
plt.xlabel('Day')
plt.ylabel('Sales')

plt.show()