EMPLOYEES = 3

count_of_students_first_employee_per_hour = int(input())
count_of_students_second_employee_per_hour = int(input())
count_of_students_third_employee_per_hour = int(input())
students_count = int(input())

all_employees = count_of_students_first_employee_per_hour + count_of_students_second_employee_per_hour + count_of_students_third_employee_per_hour
hours = 0

while students_count > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    students_count -= all_employees

print(f"Time needed: {hours}h.")


