
budget = float(input())
flour_price_1kg = float(input())


pack_of_eggs = flour_price_1kg * 0.75
price_of_milk_1l = (flour_price_1kg * 0.25) + flour_price_1kg
price_of_milk_250ml = price_of_milk_1l * 0.25

total_price_cozonac = flour_price_1kg + pack_of_eggs + price_of_milk_250ml

colored_eggs = 0
cozonac = 0

while budget > total_price_cozonac:

    budget -= total_price_cozonac

    cozonac += 1
    colored_eggs += 3

    if cozonac % 3 == 0:
        colored_eggs -= (cozonac - 2)

print(f"You made {cozonac} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")






