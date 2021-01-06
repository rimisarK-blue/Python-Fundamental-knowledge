
number = int(input())

parking_lot = {}

for _ in range(number):
    data = input().split()
    if data[0] == "register":
        driver = data[1]
        car_number = data[2]
        if driver not in parking_lot:
            parking_lot[driver] = car_number
            print(f"{driver} registered {car_number} successfully")
        else:
             print(f"ERROR: already registered with plate number {car_number}")
    elif data[0] == "unregister":
        driver = data[1]
        if driver not in parking_lot:
             print(f"ERROR: user {driver} not found")
        else:
            parking_lot.pop(driver)
            print(f"{driver} unregistered successfully")


for user, plate in parking_lot.items():
    print(f"{user} => {plate}")