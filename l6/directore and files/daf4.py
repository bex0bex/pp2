import os

def task(path, l):
    with open(path, 'w') as file:
        file.write(' '.join(l))