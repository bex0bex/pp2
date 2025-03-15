
import os

def task(path1, path2):
    with open(path1, 'r') as file1, open(path2, 'a') as file2:
        file2.write(file1.read())