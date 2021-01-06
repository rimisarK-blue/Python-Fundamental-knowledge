
data = input()

memory = {}

for el in data:
    if not el == ' ':
        if el in memory:
            memory[el] += 1
        else:
            memory[el] = 1


for char, occurrences in memory.items():
    print(f"{char} -> {occurrences}")