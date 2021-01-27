import re

data = input()

pattern = r"\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b"

matching = re.findall(pattern, data)
for match in matching:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}", )