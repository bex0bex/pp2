import re 

a = r'^ab*$'
b = input().split() 

for i in b:
    if re.fullmatch(a, i):
        print("true")
    else: print("false")
