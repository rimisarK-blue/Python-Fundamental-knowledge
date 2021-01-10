
numbers = input().split()
numbers_to_remove = int(input())


for index in range(len(numbers)):
    numbers[index] = int(numbers[index])

for index in range(numbers_to_remove):
    numbers.remove(min(numbers))

print(numbers)