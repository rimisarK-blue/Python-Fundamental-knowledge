
sequence = [int(el) for el in (input().split())]

def shoot(nums,i,v):
    if 0 <= i < len(nums):
        nums[i] -= v
        if nums[i] <= 0:
            nums.pop(i)
    return nums
def add(nums,i,v):
    if 0 <= i < len(nums):
        nums.insert(i,v)
    else:
        print("Invalid placement!")
    return nums
def strike(nums,i,v):
    left_index = i - v
    right_index = i + v
    if left_index >= 0 and right_index < len(nums):
        left_part = nums[:left_index]
        right_part = nums[right_index+1:]
        nums = left_part + right_part
    else:
        print("Strike missed!")
    return nums


command = input()
while command != 'End':
    action, index ,value = command.split()
    index = int(index)
    value = int(value)
    if action == 'Shoot':
        sequence = shoot(sequence,index,value)
    elif action == 'Add':
        sequence = add(sequence, index, value)
    elif action == 'Strike':
        sequence = strike(sequence, index, value)

    command = input()

print('|'.join(map(str,sequence)))