"""
Q2. — Easy
Using the same DataFrame:
df = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [75, None, 82, None]
})
Create a new version of the DataFrame where missing marks values are replaced with 0.
Print the result.
Think about why replacing missing values might be useful before performing calculations.
"""

import pandas as pd

df = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [75, None, 82, None]
})

df_new = df.fillna(0)
print(df_new)