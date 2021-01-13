
houses = list(int(el) for el in input().split('@'))

position = 0


command = input()
while not command == "Love!":
    action = command.split()
    jump = int(action[1])

    if position + jump > len(houses) -1 :
        position = 0
        jump = 0
    if houses[position + jump] == 0:
        print(f"Place {position + jump} already had Valentine's day.")
    else:
        houses[position + jump] -= 2
        if houses[position + jump] == 0:
           print(f"Place {position + jump} has Valentine's day." )

    position += jump
    command = input()

print(f"Cupid's last position was {position}.")
failed = 0
for el in houses:
    if el != 0:
        failed += 1
if failed == 0:
 print("Mission was successful.")
else:
 print(f"Cupid has failed {failed} places.")






