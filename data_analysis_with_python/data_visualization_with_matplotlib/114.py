"""
Q14. — Mixed
You have this Pandas DataFrame:
sales = pd.DataFrame({
"month": ["Jan", "Feb", "Mar", "Apr", "May"],
"sales": [12000, 15000, 13500, 18000, 21000]
})
Create a visualization directly from the DataFrame that shows how sales changed from January
to May.
"""

import matplotlib.pyplot as plt
import pandas as pd

sales = pd.DataFrame({
"month": ["Jan", "Feb", "Mar", "Apr", "May"],
"sales": [12000, 15000, 13500, 18000, 21000]
})

plt.plot(sales['month'], sales['sales'], marker='o')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales')

plt.show()