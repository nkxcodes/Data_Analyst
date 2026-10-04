"""
Q2. — Easy
Create a Pandas DataFrame containing this student data:
Name Marks
Rahul 78
Priya 85
Aman 62
Print the DataFrame.
Then identify which part represents the columns and which part represents the rows.
"""

import pandas as pd

data = {
    'Name': ['Rahul', 'Priya', 'Aman'],
    'Marks': [78, 85, 62]
}

df = pd.DataFrame(data)
print(df)