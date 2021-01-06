
command = input()

volt = {}

while not command == "stop":
    value = int(input())
    if command in volt:
        volt[command] += value
    else:
        volt[command] = value

    command = input()

for resource, quantity in volt.items():
    print(f"{resource} -> {quantity}")