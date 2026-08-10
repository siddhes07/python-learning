salary = float(input("Enter your annual salary: "))

if salary <= 300000:
    tax = 0

elif salary <= 600000:
    tax = salary * 0.05

elif salary <= 1200000:
    tax = salary * 0.10

elif salary <= 2000000:
    tax = salary * 0.20

else:
    tax = salary * 0.30

final_salary = salary - tax

print("Annual Salary:", salary)
print("Tax:", tax)
print("Salary After Tax:", final_salary)