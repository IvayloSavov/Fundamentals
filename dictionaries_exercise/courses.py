from _collections import defaultdict

courses = defaultdict(list)

while True:
    command = input()
    if command == "end":
        break
    course_name, student_name = command.split(" : ")
    courses[course_name].append(student_name)

courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))

for course_name, students in courses.items():
    students = list(sorted(students))
    print(f"{course_name}: {len(students)}")
    for student in students:
        print(f"-- {student}")

