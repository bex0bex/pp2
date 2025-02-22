import re

f = open("raw.txt", "r",encoding="utf-8")
text = f.read()

def match_string(s):
    pattern = r'^ab*$'  
    if re.fullmatch(pattern, s):
        return True
    else:
        return False