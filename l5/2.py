import re

def match_ab_two_to_three(s):
    return bool(re.fullmatch(r'^ab{2,3}$', s))