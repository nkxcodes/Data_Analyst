"""
Q8.​
You are creating a simple login check.
Store a username and password in variables.
The user should be allowed to log in only when both the username and password are correct.
Otherwise, display an appropriate failure message.
"""

correct_username = 'admin'
correct_password = '1234'

username = input('Enter your username: ')
password = input('Enter password: ')

if (username == correct_username and
    password == correct_password):
    print('Logged in')
else:
    print('Incorrect credentials!')