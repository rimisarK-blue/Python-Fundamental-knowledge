
gifts = input().split()

final_gifts = []
while True:
    command = input()
    if "No Money" in command:
        break
    elif "OutOfStock" in command:
        command_list = command.split()
        for i in range(len(gifts)):
            if command_list[1] == gifts[i]:
                gifts[i] = 'None'

    elif "Required" in command:
        command_list = command.split()
        for i in range(len(gifts)):
            if i == int(command_list[2]):
                gifts[i] = command_list[1]

    elif "JustInCase" in command:
        command_list = command.split()
        gifts.remove(gifts[-1])
        gifts.append(command_list[1])

for i in range(len(gifts)):
    if gifts[i] != 'None':
        final_gifts.append(str(gifts[i]))

print(' '.join(final_gifts))










