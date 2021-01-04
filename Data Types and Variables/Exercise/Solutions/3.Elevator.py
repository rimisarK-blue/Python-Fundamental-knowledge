
people = int(input())
capacity = int(input())

courses = 0

for i in range(people, 0, -capacity):
    courses += 1
print(courses)


