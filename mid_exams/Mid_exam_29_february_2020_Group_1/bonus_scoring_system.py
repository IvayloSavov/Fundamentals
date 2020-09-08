from sys import maxsize
from math import ceil
count_of_students = int(input())
count_of_lectures = int(input())
bonus = int(input())

max_bonus_student = 0
student_attendance_max = 0
total_bonus = 0

for student in range(count_of_students):
    student_attendances = int(input())
    total_bonus = (student_attendances / count_of_lectures * (5 + bonus))
    if total_bonus >= max_bonus_student:
        max_bonus_student = total_bonus
        student_attendance_max = student_attendances


print(f"Max Bonus: {ceil(max_bonus_student)}.")
print(f"The student has attended {student_attendance_max} lectures.")
