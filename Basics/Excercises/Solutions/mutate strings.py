string_1 = input()
string_2 = input()

current_str = ''
previous_str = string_1

for iteration in range(len(string_1)):
    for index_str_2 in range(0, iteration+1):
        current_str += string_2[index_str_2]
    for index_str_1 in range(iteration +1, len(string_1)):
        current_str += string_1[index_str_1]
    if not previous_str == current_str:
        print(current_str)
        previous_str = current_str
    current_str = ''