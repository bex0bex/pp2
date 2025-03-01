import re

text = input("Enter CamelCase string: ")
words = re.findall(r'[A-Z][a-z]*', text)

print("Words:", words)