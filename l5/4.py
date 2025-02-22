import re
def find_upper_followed_by_lower(s):
    return re.findall(r'\b[A-Z][a-z]+\b', s)