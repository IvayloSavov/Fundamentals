def grading_students(list_grades):
    for index, grade in enumerate(list_grades):
        if grade < 38:
            continue

        next_number_multiplied_by_five = 0

        for number in range(grade + 1, grade + 100):
            if number % 5 == 0:
                next_number_multiplied_by_five = number
                break

        if (next_number_multiplied_by_five - grade) < 3:
            list_grades[index] = next_number_multiplied_by_five

    list_grades = list(map(str, list_grades))
    return print("\n".join(list_grades))


number_of_students = int(input())
grades = []

for _ in range(number_of_students):
    current_student_grade = int(input())
    grades.append(current_student_grade)

grading_students(grades)
