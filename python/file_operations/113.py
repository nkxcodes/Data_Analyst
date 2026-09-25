"""
Q13. — Mixed
You have:
numbers.txt
containing one number per line.
Create a program that:
1.​ Reads all the numbers.
2.​ Converts them into integers.
3.​ Finds only the even numbers.
4.​ Writes those even numbers into a new file called even_numbers.txt.
Use file operations, lists, loops, and conditions.
"""

with open('numbers.txt', 'r') as file:
    content = file.read()
    content = content.split()
    numbers = []

    for value in content:
        numbers.append(int(value))

    with open('even_numbers.txt', 'w') as file:
        for num in numbers:
            if num % 2 == 0:
                file.write(f'{num}\n')