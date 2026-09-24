"""
Q4. — Medium
You have a file called story.txt.
Read the file and determine:
1.​ How many characters it contains.
2.​ How many lines it contains.
3.​ How many words it contains.
Do not count the newline character as a word.
"""

with open('story.txt', 'r') as file:
    reader = file.read()

    print(f'Characters: {len(reader)}')

    reader = reader.split('\n')

    words = 0
    lines = 0
    for line in reader:
        lines += 1
        
        line = line.split()
        for word in line:
            words += 1
        
    print(f'Lines: {lines}')
    print(f'Words: {words}')