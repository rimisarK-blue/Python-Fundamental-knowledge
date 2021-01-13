import math
numbers = [int(el) for el in input().split(', ')]

boundery = 10
previous_boundery = 0
removed_numbers = []
rounding = (math.ceil(max(numbers) / 10.0)) * 10

while rounding >= boundery:
    for el in numbers:
        if previous_boundery < el <= boundery:
            removed_numbers.append(el)
    print(f'Group of {boundery}\'s: {removed_numbers}')
    removed_numbers = []
    boundery += 10
    previous_boundery += 10
