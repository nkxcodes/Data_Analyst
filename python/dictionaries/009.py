"""
Q9.​
You have a sentence such as:
"python is easy and python is powerful"
Create a dictionary that counts how many times each word appears in the sentence.
For this question, think about how the dictionary can keep track of information that changes as
you process each word.
"""

sentence = 'python is easy and python is powerful'
sentence = sentence.split()

word_count = {}

for word in sentence:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)