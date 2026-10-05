"""
Q10. — Tricky
Consider:
df = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [70, None, 80, None]
})
what happens to the average marks if you calculate the average directly while the
DataFrame still contains missing values.
Then compare that with replacing the missing values with 0 before calculating the average.
Why are the two averages different?
The important part is not just getting the numbers — explain what the missing values mean in
each situation.
"""

import pandas as pd

df = pd.DataFrame({
"name": ["Aman", "Priya", "Rahul", "Neha"],
"marks": [70, None, 80, None]
})

"""
mean() with missing values asks 'What is the average of the known marks?'
while fillna(0).mean() asks 'What is the average if every missing
marks is treated as zero?'
"""