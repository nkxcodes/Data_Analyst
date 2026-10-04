"""
Q1. — Easy
Given:
df = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [75, None, 82, None]
})
Find out which values are missing in the DataFrame.
Then find the total number of missing values.
"""

import pandas as pd

df = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [75, None, 82, None]
})

print()
print(df.isnull().sum())

print()
print(df.isnull().any())

print()
print(df.isnull().sum().sum())