
num_lines = int(input())

count = 0

for i in range(num_lines, 0, -1):
    character = input()
    count += ord(character)

print(f'The sum equals: {count}')
