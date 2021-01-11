

nums = [int(el) for el in input().split(', ')]

even_numbers = [index for index in range(len(nums)) if nums[index] % 2 == 0 ]

print(even_numbers)