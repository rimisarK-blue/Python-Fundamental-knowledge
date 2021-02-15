
def drive(all_cars, car, dis, gas):
    current_fuel = all_cars[car]['Fuel']
    if current_fuel <= gas:
        print("Not enough fuel to make that ride")
    else:
        all_cars[car]['Mile'] += dis
        all_cars[car]['Fuel'] -= gas
        print(f"{car} driven for {dis} kilometers. {gas} liters of fuel consumed.")
    if all_cars[car]['Mile'] >= 100000:
        del all_cars[car]
        print(f"Time to sell the {car}!")
    return all_cars


def refuel(all_cars, car, gas):
    current_fuel = all_cars[car]['Fuel']
    refuel_tank = current_fuel + gas
    if refuel_tank >= 75:
        all_cars[car]['Fuel'] = 75
        print(f"{car} refueled with {75 - current_fuel} liters")
    else:
        all_cars[car]['Fuel'] = refuel_tank
        print(f"{car} refueled with {gas} liters")
    return all_cars


cars = {}
number = int(input())

for _ in range(number):
    data = input().split('|')
    brand_name = data[0]
    mileage = int(data[1])
    fuel = int(data[2])
    cars[brand_name] = {'Mile': mileage, 'Fuel': fuel}

command = input()
while not command == 'Stop':
    data = command.split(' : ')
    command = data[0]
    if command == "Drive":
        car_name, distance, fuel = data[1:]
        distance = int(distance)
        fuel = int(fuel)
        cars = drive(cars, car_name, distance, fuel)

    elif command == "Refuel":
        car, fuel = data[1:]
        fuel = int(fuel)
        cars = refuel(cars, car, fuel)

    elif command == "Revert":
        car, kilometer = data[1:]
        kilometer = int(kilometer)
        decreased_mile = cars[car]['Mile'] - kilometer

        if decreased_mile <= 10000:
            cars[car]['Mile'] = 10000
        else:
            cars[car]['Mile'] = decreased_mile
            print(f"{car} mileage decreased by {kilometer} kilometers")

    command = input()


sorted_cars = sorted(cars.items(), key=lambda x: (-x[1]["Mile"], x[0]))

for car, value in sorted_cars:
    print(f"{car} -> Mileage: {value['Mile']} kms, Fuel in the tank: {value['Fuel']} lt.")
