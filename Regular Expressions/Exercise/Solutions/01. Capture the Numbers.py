import re

data = ""
new_data = input()
while True:
    if len(new_data) == 0:
        break
    data += " "
    data += new_data
    new_data = input()

pattern = r"\d+"

numbers = re.findall(pattern, data)

print(*numbers)