
data = input()

current_result = ""
result = ""
index = 0
while index < len(data):
    if not data[index].isdigit():
        current_result += data[index]
        index += 1
    else:
        number = ''
        while index < len(data) and data[index].isdigit():
            number += data[index]
            index += 1

        number = int(number)
        current_result = current_result.upper() * number
        result += current_result
        current_result = ''

print(f"Unique symbols used: {len(set(result))}")
print(result)