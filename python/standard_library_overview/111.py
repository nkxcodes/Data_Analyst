"""
Q11. — Tricky
A beginner writes:
import json
student = {
"name": "Aman",
"marks": 85
}
data = json.dumps(student)
print(data["name"])
Find the mistake.
Explain what type of value data is after json.dumps() and why the indexing attempt doesn't
work as expected.
"""

import json

student = {
    "name": "Aman",
    "marks": 85
}

data = json.dumps(student)

print(data["name"])

"""
the problem is that we converted python object to json string
by using json.dumps(student), so, data becomes from dictionary
to json string. that's data["name"] is giving error.

but string are access using integer indexes, we can do data[0] etc.
"""