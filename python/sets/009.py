"""
Q9.​
A website has a list of visitors who logged in today.
Some usernames appear multiple times because users logged in more than once.
Create a program that determines:
●​ how many unique users visited,
●​ whether a particular username visited,
●​ and the names of all unique users.
"""

visitors = ['Rahul', 'Aman', 'Rahul', 'Nitesh', 'Aman', 'Priya', 'Rahul']

unique_visitors = set(visitors)

# ●​ how many unique users visited
print(len(unique_visitors))

# ●​ whether a particular username visited
print('Rahul' in unique_visitors)

# ●​ the names of all unique users.
print(unique_visitors)