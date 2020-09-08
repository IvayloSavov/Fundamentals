from sys import maxsize
employee_efficiency_one = int(input())
employee_efficiency_two = int(input())
employee_efficiency_three = int(input())
total_people_count = int(input())

hours = 0
employee_total_efficiency = employee_efficiency_one + employee_efficiency_two + employee_efficiency_three

while total_people_count > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    total_people_count -= employee_total_efficiency

print(f"Time needed: {hours}h.")
