
lines = int(input())

water_tank = 0

for i in range(0, lines):
    water = int(input())

    if water <= 255 and water_tank <= 255:
        water_tank += water
        if water_tank > 255:
            water_tank -= water
            print('Insufficient capacity!')
            continue
    else:
        print('Insufficient capacity!')
        continue

print(water_tank)

