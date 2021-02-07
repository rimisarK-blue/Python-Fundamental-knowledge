
sugar_cups = input().split()

command = input()

while not command == 'Mort':

    action = command.split()

    if action[0] == 'Add':
        sugar_cups.append(action[1])

    elif action[0] == 'Remove':
        sugar_cups.remove(action[1])

    elif action[0] == 'Replace':
        for el in sugar_cups:
             if el == action[1]:
                index_old_cup = sugar_cups.index(el)
                sugar_cups.remove(action[1])
                sugar_cups.insert(index_old_cup, action[2])
                action[1] = 'replaced'

    elif action[0] == 'Collapse':
        sugar_cups = list(int(el)for el in sugar_cups)
        collapse = int(action[1])
        for el in sugar_cups:
            if el < collapse:
                sugar_cups.remove(el)
        for el in sugar_cups:
            if el < collapse:
                sugar_cups.remove(el)
        for el in sugar_cups:
            if el < collapse:
                sugar_cups.remove(el)
        for el in sugar_cups:
            if el < collapse:
                sugar_cups.remove(el)
        sugar_cups = list(str(el)for el in sugar_cups)


    command = input()


print(" ".join(sugar_cups))




