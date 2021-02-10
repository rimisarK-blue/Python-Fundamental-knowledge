
massage = input()
command = input()

while not command == "Decode":
    data = command.split('|')
    command = data[0]
    if command == "Move":
        index = int(data[1])

        moving = massage[:index]
        remain = massage[index:]
        massage = remain + moving
    elif command == "Insert":
        index, value = data[1:]
        index = int(index)
        massage = massage[:index] + value + massage[index:]
    elif command == "ChangeAll":
        sub_string, replace = data[1:]
        massage = massage.replace(sub_string, replace)

    command = input()

print(f"The decrypted message is: {massage}")