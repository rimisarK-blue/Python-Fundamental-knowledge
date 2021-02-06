
energy = int(input())

data = input()
won_battle = 0
win = True
while not data == 'End of battle':
    distance = int(data)

    if distance > energy:
        print(f"Not enough energy! Game ends with {won_battle} won battles and {energy} energy")
        win = False
        break
    else:
        energy -= distance
        won_battle += 1
    if won_battle % 3 == 0:
        energy += won_battle

    data = input()


if win:
    print(f"Won battles: {won_battle}. Energy left: {energy}")


