"""
Q7. — Application
You have the number of visitors to a website over one week:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
visitors = [120, 150, 135, 180, 210, 260, 230]
Create a visualization that makes it easy to see how the number of visitors changed during the
week.
Choose the appropriate type of graph yourself.
"""

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
visitors = [120, 150, 135, 180, 210, 260, 230]

plt.plot(days, visitors, color='purple', marker='o')
plt.xlabel('Days')
plt.ylabel('Visitors')
plt.title('Website visitors during this week')
plt.show()