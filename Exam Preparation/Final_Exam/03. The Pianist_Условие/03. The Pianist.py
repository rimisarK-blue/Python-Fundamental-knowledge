

pieces = {}
num = int(input())

for _ in range(num):
    data = input().split('|')
    piece = data[0]
    composer = data[1]
    key = data[2]
    pieces[piece] = {'composer': composer, 'key': key}

command = input()
while not command == "Stop":
    data = command.split('|')
    command = data[0]
    if command == "Add":
        piece, composer, key = data[1:]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == "Remove":
        piece = data[1]
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        piece, new_key = data[1:]
        if piece in pieces:
            pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

sorted_pieces = sorted(pieces.items(), key=lambda x: (x[0], x[1]['composer']))

for name, value in sorted_pieces:
    print(f"{name} -> Composer: {value['composer']}, Key: {value['key']}")
