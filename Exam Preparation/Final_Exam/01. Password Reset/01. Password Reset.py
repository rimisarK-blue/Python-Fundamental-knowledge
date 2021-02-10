
def takeodd(raw_pass):
    result = ""
    for i in range(1, len(raw_pass), 2):
        result += raw_pass[i]
    print(result)
    return result


def cut(raw_data, i, leng):
    result = raw_data[:i] + raw_data[i+leng:]
    print(result)
    return result


def substitute(raw_pass, sub_s, rep):
    result = raw_pass.replace(sub_s, rep)
    if result == raw_pass:
        print("Nothing to replace!")
        return result
    else:
        print(result)
        return result



password = input()
line = input()

while not line == "Done":
    data = line.split(" ")
    command = data[0]
    if command == "TakeOdd":
        password = takeodd(password)
    elif command == "Cut":
        index, length = [int(el)for el in data[1:]]
        password = cut(password, index, length)
    elif command == "Substitute":
        sub_string, replacement = data[1:]
        password = substitute(password, sub_string, replacement)

    line = input()

print(f"Your password is: {password}")