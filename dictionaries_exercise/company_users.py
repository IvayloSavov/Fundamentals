from _collections import defaultdict

companies = defaultdict(list)

while True:
    command = input()
    if command == "End":
        break
    company_name, employee_id = command.split(" -> ")
    if employee_id in companies[company_name]:
        continue
    companies[company_name].append(employee_id)

companies = dict(sorted(companies.items(), key=lambda x: x[0]))

for company_name, employee_id in companies.items():
    print(company_name)
    for employee in employee_id:
        print(f"-- {employee}")