
n = int(input())

positive = []
negative = []

for iteration in range(n):
    current_num = int(input())

    if current_num > 0:
        positive.append(current_num)
    else:
        negative.append(current_num)

print(positive)
print(negative)

print(f'Count of positives: {len(positive)}. Sum of negatives: {sum(negative)}')

