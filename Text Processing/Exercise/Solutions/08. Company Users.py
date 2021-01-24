position_alphabet = {chr(ele+97): ele+1 for ele in range(26)}


data = input().split()
result = 0
for el in data:
    first_el = el[0]
    last_el = el[-1]
    number = int(el[1:-1])
    if first_el.isupper():
        number /= position_alphabet[first_el.lower()]
    elif first_el.islower():
        number *= position_alphabet[first_el]
    if last_el.isupper():
        number -= position_alphabet[last_el.lower()]
    elif last_el.islower():
        number += position_alphabet[last_el]

    result += number

print(f"{result:.2f}")
