import re
phone_numbers = input()

correct_form = r"(\+359\s2\s\d{3}\s\d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"

matches = re.finditer(correct_form, phone_numbers)

matches = [p.group(0) for p in matches]

print(", ".join(matches))