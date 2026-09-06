employees = []

n = int(input("Enter number of employees: "))

for i in range(n):

    print("\nEmployee", i + 1)

    name = input("Enter name: ")
    department = input("Enter department: ")

    salary = []

    for j in range(3):
        s = int(input(f"Enter salary of month {j + 1}: "))
        salary.append(s)

    employee = (name, department, salary)

    employees.append(employee)


highest_average = -1
highest_employee = ""

print("\n========== EMPLOYEE DETAILS ==========")

for employee in employees:

    name = employee[0]
    department = employee[1]
    salary = employee[2]

    total = 0

    for s in salary:
        total = total + s

    average = total / 3

    if average > 30000:
        status = "High Salary"
    else:
        status = "Normal Salary"

    print("\nName:", name)
    print("Department:", department)
    print("Salary:", salary)
    print("Total:", total)
    print("Average:", average)
    print("Status:", status)

    if average > highest_average:
        highest_average = average
        highest_employee = name


print("\n========== HIGHEST SALARY ==========")
print("Employee:", highest_employee)
print("Average Salary:", highest_average)


print("\n========== IT DEPARTMENT ==========")

for employee in employees:

    name = employee[0]
    department = employee[1]

    if department.lower() == "it":
        print(name)