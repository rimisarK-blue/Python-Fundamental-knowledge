
parameters = int(input())
count = int(input())

numbers = []
multiplier = 0
for num in range(0, count):
    multiplier += parameters

    if multiplier == parameters:
        numbers.append(multiplier)
        continue
    if multiplier != parameters:
        numbers.append(multiplier)
        continue

print(numbers)




