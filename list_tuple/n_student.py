students = []

n = int(input("Enter number of students: "))

# Taking input
for i in range(n):

    name = input("\nEnter student name: ")

    marks = []

    print("Enter marks of 5 subjects:")

    for j in range(5):
        mark = int(input(f"Subject {j + 1}: "))
        marks.append(mark)

    # Store name and marks as tuple
    student = (name, marks)

    students.append(student)


# Find total and average
highest_average = -1
top_student = ""

print("\n----- Student Result -----")

for student in students:

    name = student[0]
    marks = student[1]

    total = 0

    for mark in marks:
        total = total + mark

    average = total / 5

    if average >= 75:
        grade = "Excellent"
    else:
        grade = "Needs Improvement"

    print("\nName:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Result:", grade)

    # Finding highest average
    if average > highest_average:
        highest_average = average
        top_student = name


print("\n---------------------------")
print("Top Student:", top_student)
print("Highest Average:", highest_average)