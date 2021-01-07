data = input()

company_employees = {}

while not data == "End":
    company, employee_id = data.split(" -> ")

    if company not in company_employees:
        company_employees[company] = []
    if employee_id not in company_employees[company]:
        company_employees[company].append(employee_id)

    data = input()

for company, employee_ids in sorted(company_employees.items(), key=lambda x: x[0]):
    print(f"{company}")
    for id in employee_ids:
        print(f"-- {id}")

