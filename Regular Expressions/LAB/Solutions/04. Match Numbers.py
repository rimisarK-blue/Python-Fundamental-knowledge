import re

data = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

numbers = re.finditer(pattern, data)

numbers = [n.group(0) for n in numbers]

print(*numbers)


