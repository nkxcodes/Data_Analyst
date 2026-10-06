"""
Q8. — Application
A shop has the following product sales:
products = ["Pen", "Notebook", "Bag", "Bottle"]
sales = [120, 80, 35, 60]
Create a visualization that makes it easy to compare the sales of the four products.
Then make the graph readable by adding an appropriate title and labels.
"""

import matplotlib.pyplot as plt

products = ["Pen", "Notebook", "Bag", "Bottle"]
sales = [120, 80, 35, 60]

plt.bar(products, sales, color='purple')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Product Sales Comparison')
plt.show()