import re


pattern = r'\b[a-z]+_[a-z]+\b'
text = input("Enter text: ")

matches = re.findall(pattern, text)
print("Matches:", matches)