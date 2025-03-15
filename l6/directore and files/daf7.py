import os

def task(path):
    if os.access(path, os.F_OK):
        os.remove(path)
        print('File exists and has been removed')
    else:
        print(f"Error: File '{path}' does not exist.")