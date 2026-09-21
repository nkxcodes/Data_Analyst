"""
Q12. — Tricky
You want to find all phone numbers inside this text:
"Call Rahul at 9876543210 or Aman at 9123456780."
Use the re module to search for 10-digit numbers.
Then consider this question:
Why would a regular expression be more useful here than simply using split()?
"""

import re

text = "Call Rahul at 9876543210 or Aman at 9123456780"

print(re.findall("\d{10}", text))