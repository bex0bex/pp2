import re

pattern = r'^a.*b$'
words = input("Enter words: ").split()

for word in words:
    print("true" if re.fullmatch(pattern, word) else "false")