"""
Q11. — Tricky — Find the mistake
A beginner has this DataFrame:
df = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul"],
"age": ["17", "18", "17"]
})
They write:
df["age"].astype(int)
print(df)
But they expect the DataFrame's age column to permanently become integers.
Find the mistake in their thinking.
Explain what happens to the result of astype() and what needs to be done if they want the
DataFrame itself to contain the changed datatype.
"""

import pandas as pd

df = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul"],
"age": ["17", "18", "17"]
})

df['age'] = df["age"].astype(int)
print(df)