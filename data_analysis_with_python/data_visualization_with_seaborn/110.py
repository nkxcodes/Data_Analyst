"""
Q10. — Tricky — Predict first
Before running this code, predict what the plot will show:
import seaborn as snsimport pandas as pdimport matplotlib.pyplot as pltdata = pd.DataFrame({
"category": ["A", "B", "C"], "value": [10, 20, 30]})sns.barplot(data=data, x="category",
y="value")plt.show()
Answer these questions:
1.​ What determines the height of each bar?
2.​ Does a Seaborn bar plot always display every individual observation directly?
3.​ If each category contained several values, what would the bars generally represent by
default?
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame({
"category": ["A", "B", "C"], "value": [10, 20, 30]
})

sns.barplot(x='category', y='value', data=data)

plt.show()

"""
1. y = 'value' determines the height of each bar.
2. No, A seaborn bar plot displays the mean (average)
by default, not every individual observation.
3. If each category contained several values, the bars 
would generally represent the mean(average) of the values
in each category by default.
"""