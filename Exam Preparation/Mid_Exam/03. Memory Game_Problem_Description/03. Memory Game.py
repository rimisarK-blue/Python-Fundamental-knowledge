
memory_cards = input().split()


def play_round(cards, i1, i2, round_num):
    if i1 == i2 or i1 not in range(len(cards)) or i2 not in range(len(cards)):
        print("Invalid input! Adding additional elements to the board")
        card = f"-{round_num}a"
        middle = len(cards) // 2
        cards.insert(middle, card)
        cards.insert(middle + 1, card)
        return cards
    if cards[i1] == cards[i2]:
        element = cards[i1]
        print(f"Congrats! You have found matching elements - {element}!")
        cards.remove(element)
        cards.remove(element)
        return cards
    else:
        print("Try again!")
        return cards


command = input()
counter = 0
while not command == "end":
    index_1, index_2 = (list(map(int, command.split())))
    counter += 1
    memory_cards = play_round(memory_cards, index_1, index_2, counter)
    if len(memory_cards) == 0:
        print(f"You have won in {counter} turns!")
        break

    command = input()

if len(memory_cards) > 0:
    print("Sorry you lose :(")
    print(" ".join(memory_cards))