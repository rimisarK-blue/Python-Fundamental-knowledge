
product_prices = {}
product_quantities = {}

data = input()

while not data == "buy":
    product, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if product not in product_prices:
        product_prices[product] = price
        product_quantities[product] = quantity
    else:
        product_prices[product] = price
        product_quantities[product] += quantity

    data = input()

for product, price in product_prices.items():
    print(f"{product} -> {price * product_quantities[product]:.2f}")