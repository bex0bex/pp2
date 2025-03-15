import os
import string

def text(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for letter in string.ascii_uppercase:
        file_path = os.path.join(directory, f"{letter}.txt")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"This is file {letter}.txt\n")

directory = input("Enter : ")
text(directory)