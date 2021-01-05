food = input().split()

products = {}

for index in range(0, len(food), 2):
    key = food[index]
    value = food[index + 1]
    products[key] = int(value)

print(products)