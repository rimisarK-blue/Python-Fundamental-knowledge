food = input().split()

products = {}

for index in range(0, len(food), 2):
    key = food[index]
    value = food[index + 1]
    products[key] = int(value)

searched_products = input().split()

for product in searched_products:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
