"""
Q1. — Easy
Import Seaborn and Pandas.
Create a DataFrame containing the following data:
DayTemperature
Mon28
Tue30
Wed29
Thu32
Fri35
Create a line plot showing how the temperature changes over the five days.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Day": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    "Temperature": [28, 30, 29, 32, 35]
})

sns.lineplot(x='Day', y='Temperature', data=df)
plt.title('Temperature Changes Over Five Days')
plt.xlabel('Day')
plt.ylabel('Temperature (C)')

plt.show()