
numbers = input().split(', ')
num_of_beggars = int(input())

profit = []

for index in range(num_of_beggars):
    profit.append(0)
index = 0
while len(numbers) > 0:
    numbers[0] = int(numbers[0])
    if index < len(profit):
        profit[index] += numbers[0]
    else:
        index = 0
        continue
    numbers.pop(0)
    index += 1
print(profit)



