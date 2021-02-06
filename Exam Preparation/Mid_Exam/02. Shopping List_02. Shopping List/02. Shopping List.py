
items = input().split('!')


def check_if_exists(item_list, item_searched):
    return True if item_searched in item_list else False


command = input()
while not command == "Go Shopping!":

    command_type = command.split()[0]
    item = command.split()[1]

    if command_type == "Urgent":
        if not check_if_exists(items, item):
            items.insert(0, item)

    elif command_type == "Unnecessary":
        if check_if_exists(items, item):
            items.remove(item)

    elif command_type == "Correct":
        if check_if_exists(items, item):
            new_item = command.split()[2]
            current_item = items.index(item)
            items[current_item] = new_item

    elif command_type == "Rearrange":
        if check_if_exists(items, item):
            items.remove(item)
            items.append(item)

    command = input()


print(", ".join(items))
