
data = input()

products = {}

while not data == "statistics":
    product, quantity = data.split(': ')
    quantity = int(quantity)
    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity

    data = input()

print('Products in stock:')
for prod_name, prod_quantity in products.items():
    print(f"- {prod_name}: {prod_quantity}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")