"""
Q10. — Tricky
what Pandas will return in each case:
marks = pd.Series([50, 60, 70, 80])
What is the difference between:
marks[0]
and:
marks[[0, 2]]
Then explain why one returns a single value while the other returns a Series.
"""

import pandas as pd

marks = pd.Series([50, 60, 70, 80])

print(marks[0]) # 50
print(marks[[0, 2]]) # 50, 70

"""
marks[0] selects one index, so Pandas returns as single
value.
marks[[0, 2]] selects multiple indexes, so Pandas returns
a Series containing those values and their indexes.
"""