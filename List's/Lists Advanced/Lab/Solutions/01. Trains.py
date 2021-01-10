
num_of_waggons = int(input())

train = [int(0)for _ in range (num_of_waggons)]

command = input()

while True:
    data = command.split()

    if data[0] == 'add':
        people = int(data[1])
        train[-1] += people

    elif data[0] == 'insert':
        index = int(data[1])
        people = int(data[2])
        train[index] += people
    elif data[0] == 'leave':
        index = int(data[1])
        people = int(data[2])
        train[index] -= people
    if data[0] == 'End':
        break

    command = input()

print(train)



