
events = input().split('|')

energy = 100
coins = 100

good_day = True

for com in events:
    command, value = com.split('-')
    value = int(value)

    if command == 'rest':

        if energy == 100:
            print("You gained 0 energy.")
            print(f"Current energy: 100.")

        elif energy + value > 100:
            print(f"You gained {value} energy.")
            print(f"Current energy: 100.")

        else:
            energy += value
            print(f"You gained {value} energy.")
            print(f"Current energy: {energy}.")

    elif command == 'order':
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")

        else:
            energy += 50
            print("You had to rest!")

    else:

        if coins - value > 0:
            coins -= value
            print(f"You bought {command}.")
        else:
            good_day = False
            print(f"Closed! Cannot afford {command}.")
            break

if good_day and coins > 0 and energy > 0:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")




