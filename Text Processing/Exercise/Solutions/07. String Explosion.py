
line = input().split('>')

explode = 0

remaining = []

for step in line:
    if step[0].isdigit():
        explode += int(step[0])
        if len(step) <= explode:
            explode -= len(step)
            step = '>'
        else:
            step = '>'+''.join(list(step[explode::]))
            explode = 0
    remaining.append(step)
print("".join(remaining))