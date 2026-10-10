"""
Q12. — Tricky — Understand the visualization
Consider this code:
sns.histplot(data=df, x="marks", bins=5)
Predict how the histogram might change if you changed bins=5 to bins=10.
Explain:
1.​ What a bin represents.
2.​ Why changing the number of bins changes the appearance of a histogram.
3.​ Why a histogram is suitable for numerical distributions but is not usually the best choice
for comparing unrelated categories such as student names.
"""

"""
1. A bin represent an interval or group of numerical values
in a histogram. Each bar shows how many observations fall
within that interval.
2. Changing the number of bins changes the width and number
of intervals. More bins generally create narrower intervals
and show more detail, while fewer bins create wider intervals
and provide a broader view of the distribution.
3. A histogram is suitable for numerical data because it
groups values into intervals and shows their frequency.
Student names are unrelated categories, so a bar plot
is usually more appropriate for comparing them.
"""