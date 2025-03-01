import re
text = input("Enter CamelCase/PascalCase string: ")
result = re.sub(r'([A-Z])', r' \1', text).strip()

print("Modified text:", result)