"""
Q9. — Application
A business has customer data:
customers = pd.DataFrame({ "age": [18, 22, 25, 30, 35, 40, 45, 50], "spending": [200, 250,
300, 400, 450, 500, 550, 650], "membership": ["Basic", "Basic", "Premium", "Basic",
"Premium", "Premium", "Basic", "Premium"]})
Create a visualization that helps the business explore the relationship between customer age
and spending.
Also distinguish the two membership types visually.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customers = pd.DataFrame({ "age": [18, 22, 25, 30, 35, 40, 45, 50], "spending": [200, 250,
300, 400, 450, 500, 550, 650], "membership": ["Basic", "Basic", "Premium", "Basic",
"Premium", "Premium", "Basic", "Premium"]
})

sns.scatterplot(x='age', y='spending', hue='membership',data=customers, marker='x')

plt.show()