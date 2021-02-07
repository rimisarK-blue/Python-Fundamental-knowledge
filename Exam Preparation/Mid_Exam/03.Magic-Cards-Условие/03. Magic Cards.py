
available_cards = input().split(':')
new_deck = []
command = input()

while not command == 'Ready':
    action = command.split()
    if action[0] == 'Add':
        if not action[1] in available_cards:
            print("Card not found.")
        for el in available_cards:
            if action[1] == el:
                new_deck.append(el)

    elif action[0] == 'Insert':
        ind = int(action[2])
        if ind < len(new_deck) and ind > 0:
            new_deck.insert(ind, action[1])
        else:
            print("Error!")

    elif action[0] == 'Remove':
        if action[1] in new_deck:
            new_deck.remove(action[1])
        else:
            print("Card not found.")

    elif action[0] == 'Swap':
        for el in new_deck:
            if el == action[1] :
                index_first_monster = new_deck.index(el)

            if el == action[2]:
                index_second_monster = new_deck.index(el)
        new_deck[index_first_monster], new_deck[index_second_monster] = new_deck[index_second_monster], new_deck[index_first_monster]

    elif action[0] == 'Shuffle':
        new_deck.reverse()

    command = input()


print(" ".join(new_deck))









