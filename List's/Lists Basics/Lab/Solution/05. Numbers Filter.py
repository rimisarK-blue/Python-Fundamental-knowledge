
n = int(input())

even = []
odd = []
negative = []
positive = []

for iteration in range(n):
    current_num = int(input())

    if current_num % 2 == 0:
        even.append(current_num)
    if not current_num % 2 == 0:
        odd.append(current_num)
    if current_num < 0:
        negative.append(current_num)
    if current_num >= 0:
        positive.append(current_num)

command = input()

if command == "positive":
    print(positive)
if command == "negative":
    print(negative)
if command == "even":
    print(even)
if command == "odd":
    print(odd)



