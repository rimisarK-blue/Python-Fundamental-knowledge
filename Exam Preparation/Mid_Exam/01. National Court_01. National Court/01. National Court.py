first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
people_count = int(input())

hours = 0
all_people_per_hr = first_employee + second_employee + third_employee

while people_count > 0:
    hours += 1
    people_count -= all_people_per_hr

    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")

