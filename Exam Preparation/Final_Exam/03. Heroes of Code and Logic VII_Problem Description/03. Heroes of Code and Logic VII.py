def cast_spell(all_hero, hero_name, n_mana,s_name):

    current_mana = all_hero[hero_name]["MP"]
    if n_mana > current_mana:
        print(f"{hero_name} does not have enough MP to cast {s_name}!")
    else:
        all_hero[hero_name]["MP"] = current_mana - n_mana
        print(f"{hero_name} has successfully cast {s_name} and now has {all_hero[hero_name]['MP']} MP!")
    return all_hero


def take_damage(all_heros, hero_name, dm, att_name):

    current_health = all_heros[hero_name]["HP"]
    after_damage = current_health - dm
    if after_damage <= 0:
        del all_heros[hero_name]
        print(f"{hero_name} has been killed by {att_name}!")
    else:
        all_heros[hero_name]["HP"] = after_damage
        print(f"{hero_name} was hit for {dm} HP by {att_name} and now has {all_heros[hero_name]['HP']} HP left!")
    return all_heros


def recharge(all_heros, h_name, am):

    current_mana = all_heros[h_name]["MP"]
    boost_mana = current_mana + am
    if boost_mana >= 200:
        all_heros[h_name]["MP"] = 200
        print(f"{h_name} recharged for {200 - current_mana} MP!")
    else:
        all_heros[h_name]["MP"] = boost_mana
        print(f"{h_name} recharged for {am} MP!")
    return all_heros


def heal(all_heros, h_name, am):
    current_health = all_heros[h_name]["HP"]
    boost_health = current_health + am
    if boost_health >= 100:
        all_heros[h_name]["HP"] = 100
        print(f"{h_name} healed for {100 - current_health} HP!")
    else:
        all_heros[h_name]["HP"] = boost_health
        print(f"{h_name} healed for {am} HP!")
    return all_heros


heroes = {}

num = int(input())

for _ in range(num):
    data = input().split()
    name = data[0]
    hit_point = int(data[1])
    mana_point = int(data[2])
    heroes[name] = {"HP": hit_point, "MP": mana_point}

command = input()

while not command == "End":
    data = command.split(" - ")
    command = data[0]
    if command == "CastSpell":
        hero_name, need_mana, spell_name = data[1:]
        need_mana = int(need_mana)
        heroes = cast_spell(heroes,hero_name, need_mana, spell_name)

    elif command == "TakeDamage":
        hero_name, damage, attacker = data[1:]
        damage = int(damage)
        heroes = take_damage(heroes, hero_name, damage, attacker)

    elif command == "Recharge":
        hero_name, amount = data[1:]
        amount = int(amount)
        heroes = recharge(heroes, hero_name, amount)

    elif command == "Heal":
        hero_name, amount = data[1:]
        amount = int(amount)
        heroes = heal(heroes, hero_name, amount)

    command = input()

sorted_heroes = sorted(heroes.items(), key=lambda x: (-x[1]['HP'], x[0]))

for name, value in sorted_heroes:
    print(name)
    print(f"HP: {value['HP']}")
    print(f"MP: {value['MP']}")