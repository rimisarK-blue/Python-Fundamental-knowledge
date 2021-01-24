
data = input()

print("".join([symbol for index, symbol in enumerate(data) if index == 0 or symbol != data[index - 1]]))