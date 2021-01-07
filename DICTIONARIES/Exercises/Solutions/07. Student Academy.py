number = int(input())

students = {}

for _ in range(number):
    student = input()
    grade = float(input())

    if student not in students:
        students[student] = []
    students[student].append(grade)

filtered_students = {}

for name, grades in students.items():
    average_grade= sum(grades) / len(grades)
    if average_grade >= 4.50:
        filtered_students[name] = average_grade

for student, av_grade in sorted(filtered_students.items(), key=lambda x: x[1], reverse=True):
    print(f"{student} -> {av_grade:.2f}")