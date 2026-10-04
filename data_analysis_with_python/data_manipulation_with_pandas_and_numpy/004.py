"""
Q4. — Medium
Given:
df = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul"],
"age": ["17", "18", "17"],
"marks": ["75", "88", "92"]
})
Check the data types of the columns.
Then change age and marks from strings to an appropriate numeric datatype.
Check the data types again.
"""

import pandas as pd

df = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul"],
"age": ["17", "18", "17"],
"marks": ["75", "88", "92"]
})

print(df.dtypes)

df[['age', 'marks']] = df[['age', 'marks']].astype(int)

print(df.dtypes)