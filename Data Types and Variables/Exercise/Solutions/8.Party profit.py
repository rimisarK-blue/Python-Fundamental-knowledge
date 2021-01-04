
party_size = int(input())
adventure_day = int(input())

coins = 0

for n_day in range(1, adventure_day + 1):
    if n_day % 10 == 0:
        party_size -= 2
    if n_day % 15 == 0:
        party_size += 5

    coins += 50
    coins -= party_size * 2

    if n_day % 3 == 0:
        coins -= party_size * 3
    if n_day % 5 == 0:
        coins += 20 * party_size
        if n_day % 3 == 0:
         coins -= party_size * 2

print(f"{party_size} companions received {int(coins/party_size)} coins each.")






