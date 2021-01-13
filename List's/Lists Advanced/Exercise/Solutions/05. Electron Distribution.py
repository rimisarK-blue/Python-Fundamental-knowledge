
num_of_el = int(input())

electrons = []

cell_num = 1

while num_of_el > 0:
    possible_el = 2 * cell_num **2
    if num_of_el < possible_el:
        electrons.append(num_of_el)
        break
    else:
     electrons.append(possible_el)
     num_of_el -= possible_el
     cell_num +=1

print(electrons)