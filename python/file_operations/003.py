"""
Q3. — Easy
Create a file called numbers.txt containing:
10
20
30
40
50
Read the file and display each number.
"""

with open('numbers.txt', 'w') as file:
    file.write('10\n')
    file.write('20\n')
    file.write('30\n')
    file.write('40\n')
    file.write('50')

with open('numbers.txt', 'r') as file:
    print(file.read())