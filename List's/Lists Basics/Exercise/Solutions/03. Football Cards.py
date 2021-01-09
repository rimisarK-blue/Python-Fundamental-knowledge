
cards = input().split()

set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
set_2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

team_a = 11
team_b = 11


for card in cards:
    set = card.split('-')
    team = set[0]
    number = int(set[1])

    if team == 'A':
        if number in set_1:
            set_1.remove(number)
            team_a -= 1
            if team_a == 6:
                break

    elif team == 'B':
        if number in set_2:
            set_2.remove(number)
            team_b -= 1
            if team_b == 6:
                break

print(f"Team A - {team_a}; Team B - {team_b}")
if team_a == 6 or team_b == 6:
    print(f"Game was terminated")








