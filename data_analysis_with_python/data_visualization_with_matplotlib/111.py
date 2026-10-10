"""
Q11. — Tricky — Find the mistake
A beginner writes:
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Distance")
plt.title("Distance travelled")
plt.legend()
plt.show()
They expect a useful legend to appear, but there is no labelled line for the legend to describe.
Find the mistake and explain what is missing.
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y, label='Distance')
plt.xlabel("Time")
plt.ylabel("Distance")
plt.title("Distance travelled")

plt.legend()
plt.show()

"""
The mistake is that plt.plot(x, y) does not have a label
parameter. The line has no name for the legend
to display. We should add a label,
such as plt.plot(x, y, label='Distance'), so
that plt.legend() can display it.
"""