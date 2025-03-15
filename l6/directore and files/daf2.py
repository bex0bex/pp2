import os

def task(path):
    if os.path.exists(path):
        result = 'Path is '
        result += 'readable, ' if os.access(path, os.R_OK) else 'not readable, '
        result += 'writable, ' if os.access(path, os.W_OK) else 'not writable, '
        result += 'executable' if os.access(path, os.X_OK)else 'not executable.'
        print(f'Path {path} exists\n{result}')
    else:
        print(f'Path {path} does not exists')