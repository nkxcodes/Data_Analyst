"""
Q15. — Challenge
You are asked to create a small File Organizer.
Given a folder called downloads, your program should:
1.​ Look through the files in the folder.
2.​ Identify files based on their extensions.
3.​ Create appropriate folders such as Images, Documents, and Data.
4.​ Move each file into its appropriate folder.
5.​ Leave files with unknown extensions alone.
Decide yourself how to use pathlib and the file/folder operations you have already
learned.
The goal is not to make a huge program—it should simply demonstrate that you understand
how paths help Python work with real files and folders.
"""

from pathlib import Path

base_folder = Path('python/downloads')
images_folder = base_folder / 'Images'
documents_folder = base_folder / 'Documents'
data_folder = base_folder / 'Data'

for file in base_folder.iterdir():
    if file.suffix in ('.png', '.jpg', '.jpeg'):
        images_folder.mkdir(exist_ok=True)
        file.rename(images_folder / file.name)
    elif file.suffix in ('.pdf', '.txt', '.docx'):
        documents_folder.mkdir(exist_ok=True)
        file.rename(documents_folder / file.name)
    elif file.suffix in ('.csv', '.json'):
        data_folder.mkdir(exist_ok=True)
        file.rename(data_folder / file.name)