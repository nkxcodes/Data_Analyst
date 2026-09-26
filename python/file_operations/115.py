"""
Q15. — Challenge
Create a small text-file analyzer.
Given a file called article.txt, your program should:
1.​ Read the file.
2.​ Count the number of lines.
3.​ Count the number of words.
4.​ Count the number of characters.
5.​ Find how many times the word "Python" appears.
6.​ Save a short report of these results into report.txt.
Decide yourself how to organize the program and which file operations are appropriate.
"""

with open('article.txt', 'r') as file:
    content = file.read()
    characters = len(content)
    content = content.split('\n')
    
    lines = 0
    words = 0
    python_count = 0
    for line in content:
        lines += 1

        line = line.split()
        for word in line:
            words += 1
            if word == 'Python':
                python_count += 1
    
    print(f'Lines: {lines}')
    print(f'Words: {words}')
    print(f'Characters: {characters}')
    print(f'Python appeared {python_count} times')

    with open('report.txt', 'w') as file:
        file.write(f'Lines: {lines}\n')
        file.write(f'Words: {words}\n')
        file.write(f'Characters: {characters}\n')
        file.write(f'Python appeared {python_count} times\n')

    