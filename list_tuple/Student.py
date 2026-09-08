students = []

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    students.append((name, marks))


print("\nAll Students:")

for name, marks in students:
    print(name, marks)


highest = max(students, key=lambda x: x[1])
lowest = min(students, key=lambda x: x[1])

print("\nHighest:", highest[0], "-", highest[1])
print("Lowest:", lowest[0], "-", lowest[1])


total = 0

for name, marks in students:
    total += marks

average = total / len(students)

print("\nAverage:", average)


print("\nAbove Average:")

for name, marks in students:
    if marks > average:
        print(name, "-", marks)


students.sort(key=lambda x: x[1], reverse=True)

print("\nDescending Order:")

for name, marks in students:
    print(name, "-", marks)
