
data = input()

courses_and_studence = {}

while not data == 'end':
    course_name, sutudent_name = data.split(' : ')

    if course_name not in courses_and_studence:
        courses_and_studence[course_name] = []
    if sutudent_name not in courses_and_studence[course_name]:
        courses_and_studence[course_name].append(sutudent_name)

    data = input()

ordered_courses_and_studence = sorted(courses_and_studence.items(), key=lambda x: -len(x[1]),)

for course, student in ordered_courses_and_studence:
    print(f"{course}: {len(student)}")
    for id in sorted(student):
        print(f"-- {id}")





