import os

def task(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        print(f'Numbers of lines = {len(lines)}')