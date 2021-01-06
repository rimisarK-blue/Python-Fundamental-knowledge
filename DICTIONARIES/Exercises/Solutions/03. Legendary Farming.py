
mapper = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

key_material = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

while True:
    data = input().split()
    is_found = False
    for index in range(0, len(data), 2):
        quantity = int(data[index])
        item = data[index + 1].lower()

        if item in key_material:
            key_material[item] += quantity
        else:
            if item not in junk:
                junk[item] = quantity
            else:
                junk[item] += quantity

        for key, value in key_material.items():
            if value >= 250:
                print(f"{mapper[key]} obtained!")
                key_material[key] -= 250
                is_found = True
                break
        if is_found:
            break

    if is_found:
        break


ordered_key_material = sorted(key_material.items(), key=lambda x: (-x[1], x[0]))

for material, quantity in ordered_key_material:
    print(f"{material}: {quantity}")

alpha_junk = sorted(junk.items(), key=lambda x: x[0])
for material, quantity in alpha_junk:
    print(f"{material}: {quantity}")