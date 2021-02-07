
items = input().split(", ")

command = input()

while not command == "Craft!":
    data = command.split(" - ")
    command = data[0]
    if command == 'Collect':
        if not data[1] in items:
            items.append(data[1])

    elif command == "Drop":
        if data[1] in items:
            items.remove(data[1])

    elif command == "Combine Items":
        old_item, new_item = data[1].split(':')
        if old_item in items:
            item_index = items.index(old_item)
            items.insert(item_index + 1, new_item)

    elif command == "Renew":
        if data[1] in items:
            items.remove(data[1])
            items. append(data[1])

    command = input()

print(', '.join(items))