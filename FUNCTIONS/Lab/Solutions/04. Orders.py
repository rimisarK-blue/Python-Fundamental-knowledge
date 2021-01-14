
def price_calculator(item, quantity):
    if item == 'coffee':
        return 1.50 * quantity
    elif item == 'water':
        return 1.00 * quantity
    elif item == 'coke':
        return 1.40 * quantity
    elif item == 'snacks':
        return 2.00 * quantity


item_a = input()
number = int(input())
print(f'{price_calculator(item_a, number):.2f}')


