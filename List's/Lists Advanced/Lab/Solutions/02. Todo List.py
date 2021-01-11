
to_do_list = [0 for _ in range(11)]

command = input()

while not command == 'End':
    data = command.split('-')
    importance = int(data[0])
    action = data[1]
    to_do_list.insert(importance, action)

    command = input()
final_result = [task for task in to_do_list if not task == 0]
#for el in to_do_list:
   # if el != 0:
    #    final_result.append(el)

print(final_result)
