employees_happiness = input().split(" ")
happiness_improvement_factor = int(input())
employees_happiness_multiplied_by_factor = []

employees_happiness_integer = [int(employee) for employee in employees_happiness]
# employees_happiness_integer = list(map(int, employees_happiness))

for employees in employees_happiness_integer:
    happiness_multiplied = employees * happiness_improvement_factor
    employees_happiness_multiplied_by_factor.append(happiness_multiplied)

employees_happiness_multiplied_by_factor = [employees * happiness_improvement_factor for employees in employees_happiness_integer ]

count_employees = len(employees_happiness)
average_happiness = sum(employees_happiness_multiplied_by_factor) / count_employees
more_than_average_happiness = [employee for employee in employees_happiness_multiplied_by_factor
                               if employee >= average_happiness]
count_more_than_average_happiness = len(more_than_average_happiness)

if count_more_than_average_happiness >= (count_employees / 2):
    print(f"Score: {count_more_than_average_happiness}/{count_employees}. Employees are happy!")
else:
    print(f"Score: {count_more_than_average_happiness}/{count_employees}. Employees are not happy!")
