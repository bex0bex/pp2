import re

def find_lowercase_with_underscore(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)