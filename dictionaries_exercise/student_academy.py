from _collections import defaultdict

students = defaultdict(list)

students_count = int(input())

for _ in range(1, students_count + 1):
    name_student = input()
    grade_student = float(input())

    students[name_student].append(grade_student)

students = dict(sorted(students.items(), key=lambda x: -(sum(x[1]) / len(x[1]))))

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade < 4.50:
        continue
    else:
        print(f"{student} -> {average_grade:.2f}")
