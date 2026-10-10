"""
Q12. — Tricky — Understand the graph
Consider:
x = [1, 2, 3, 4, 5]
y = [10, 10, 10, 10, 10]
Create a line plot.
Then answer:
1.​ What does the graph look like?
2.​ What does the horizontal line tell you about the data?
3.​ If you changed the last value from 10 to 50, how would the graph change?
This question is about reading a visualization, not just creating one.
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 10, 10, 10, 10]

plt.plot(x, y)
plt.show()

"""
1. The graph is a horizontal straight line at y = 10
because all y-values are equal.
2. The horizontal line tells us that the y-value remains
constant even as x increases.
3. If the last value changes from 10 to 50, the graph
remains horizontal until x = 4 and then rises to y = 50
at x = 5.
"""