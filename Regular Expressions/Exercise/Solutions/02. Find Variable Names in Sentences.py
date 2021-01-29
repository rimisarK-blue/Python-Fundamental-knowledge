import re

data = input()

pattern = r"((?<=^_)|(?<=\s_))[a-zA-Z0-9]+\b"

valid = [p.group(0) for p in re.finditer(pattern, data)]
print(",".join(valid))


