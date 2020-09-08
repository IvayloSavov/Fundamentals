happiness_indexes = input().split(" ")
improvement_factor = int(input())


employees_happiness_integer = list(map(int, happiness_indexes))
employees_happiness_multiplied_by_factor = list(map(lambda n: n * improvement_factor, employees_happiness_integer))

count_employees = len(happiness_indexes)
average_happiness = sum(employees_happiness_multiplied_by_factor) / count_employees

filtered_employee = list(filter(lambda n: n >= average_happiness, employees_happiness_multiplied_by_factor))

if len(filtered_employee) >= (count_employees / 2):
    print(f"Score: {len(filtered_employee)}/{count_employees}. Employees are happy!")
else:
    print(f"Score: {len(filtered_employee)}/{count_employees}. Employees are not happy!")
