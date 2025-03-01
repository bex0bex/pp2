import re

a = r'^ab{2,3}$'
b = input().split()

for i in b:
    if re.fullmatch(a, i):
        print("true")
    else: print("false")
