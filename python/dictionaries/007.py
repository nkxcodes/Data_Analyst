"""
Q7.​
You are building a simple phone book.
Store several people's names and phone numbers in a dictionary.
Allow the program to look up a person's phone number when their name is provided.
Also handle the situation where the requested person is not in the phone book.
"""

phone_book = {
    "Rahul": "9876543210",
    "Aman": "9123456780",
    "Priya": "9988776655",
    "Manav": "9012345678",
    "Somya": "9345678901"
}

search_request = input('Enter name: ')

print(phone_book.get(search_request, 'Person not found.'))