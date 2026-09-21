"""
Q9. — Application
You have a starting date and want to calculate a future date.
Use datetime and timedelta to create a program that determines:
What date will it be 30 days after a given date?
Then modify the program to calculate a date 10 days before the given date.
"""

import datetime
from datetime import timedelta

date = datetime.datetime.now()
thirty_days = timedelta(days=30)

future_date = date + thirty_days
print(future_date)

ten_days = timedelta(days=10)
previous_date = date - ten_days

print(previous_date)