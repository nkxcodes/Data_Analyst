"""
Q11. — Tricky — Find the mistake
A beginner writes:
import seaborn as snsimport matplotlib.pyplot as pltsns.scatterplot(
x="study_hours", y="marks", hue="gender")plt.show()
data=df,
But Python raises an error saying that df is not defined.
Explain why importing Seaborn does not automatically create the DataFrame.
Correct the problem by ensuring that a suitable DataFrame exists before the plot is created.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    "study_hours": [2, 3, 4, 5, 6, 3],
    "marks": [55, 65, 72, 85, 90, 60],
    "gender": ["Male", "Female", "Male", "Female", "Male", "Female"]
})

sns.scatterplot(x='study_hours', y='marks', hue='gender', data=df, marker='x')

plt.show()

"""
Importing a library gives us access to it's tools,
it doesn't create your data automatically.
"""