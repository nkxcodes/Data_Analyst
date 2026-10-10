"""
Q7. — Application
A company tracks the monthly revenue of two products:
sales = pd.DataFrame({ "month": ["Jan", "Feb", "Mar", "Apr", "Jan", "Feb", "Mar", "Apr"],
"product": ["A", "A", "A", "A", "B", "B", "B", "B"], "revenue": [10000, 12000, 15000, 14000, 9000,
11000, 13000, 16000]})
Create a visualization that compares the monthly revenue trends of both products in one graph.
Make it clear which line belongs to which product.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sales = pd.DataFrame({ "month": ["Jan", "Feb", "Mar", "Apr", "Jan", "Feb", "Mar", "Apr"],
"product": ["A", "A", "A", "A", "B", "B", "B", "B"], "revenue": [10000, 12000, 15000, 14000, 9000,
11000, 13000, 16000]
})

sns.lineplot(x='month', y='revenue', hue='product', data=sales, marker='o')

plt.show()