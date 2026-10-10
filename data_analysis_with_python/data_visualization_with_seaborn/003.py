"""
Q3. — Easy
Create a DataFrame containing these values:
data = pd.DataFrame({
"heights": [150, 155, 160, 160, 165, 170, 170, 175, 180, 180, 185]})
Create a histogram showing the distribution of heights.
Observe how the values are grouped into intervals rather than displayed as separate
categories.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame({
"heights": [150, 155, 160, 160, 165, 170, 170, 175, 180, 180, 185]})

sns.histplot(data['heights'], bins=11, kde=True)

plt.show()