
lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

trashed_helmet = 0
trashed_sword = 0
trashed_shield = 0
trashed_armor = 0

for i in range(1, lost_fights + 1):

    if i % 2 == 0:
        trashed_helmet += 1
    if i % 3 == 0:
        trashed_sword += 1
    if i % 3 == 0 and i % 2 == 0:
        trashed_shield += 1
        if trashed_shield % 2 == 0:
            trashed_armor += 1

if trashed_armor == 0:
    armor_price == 0


total_price = (helmet_price * trashed_helmet)+(sword_price * trashed_sword)+(shield_price * trashed_shield)+(armor_price * trashed_armor)

print(f"Gladiator expenses: {total_price:.2f} aureus")





