

items = input().split(', ')


def collect(it, i):
    if i not in it:
        it.append(i)
    return it


def drop(it, i):
    if i in it:
        it.remove(i)
    return it


def combine_item(it, i):
    old_item = i.split(':')[0]
    new_item = i.split(':')[1]
    if old_item in it:
        index_old_item = it.index(old_item)
        index_new_item = index_old_item + 1
        it.insert(index_new_item, new_item)
    return it


def renew(it, i):
    if i in it:
        it.remove(i)
        it.append(i)
    return it


command = input()
while not command == "Craft!":
    action, item = command.split(' - ')

    if action == 'Collect':
        collect(items, item)
    elif action == 'Drop':
        drop(items, item)
    elif action == 'Combine Items':
        combine_item(items, item)
    elif action == 'Renew':
        renew(items, item)

    command = input()
print(', '.join(items))