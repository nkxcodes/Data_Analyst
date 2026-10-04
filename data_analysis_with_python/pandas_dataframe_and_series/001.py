"""
Q1. — Easy
Import Pandas and create a Series containing:
10, 20, 30, 40, 50
Print the Series.
Then observe what Pandas displays along with the values.
"""

import pandas as pd

data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print(series)