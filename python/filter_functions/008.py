"""
Q8. — Application
A website has a list of usernames:
usernames = ["rahul", "admin", "", "priya", "", "aman"]
The empty strings represent usernames that were not entered.
Create a result containing only the valid/non-empty usernames.
Decide yourself what condition should be used.
"""

usernames = ["rahul", "admin", "", "priya", "", "aman"]

result = filter(lambda name: name != '', usernames)

print(list(result))