marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks >= 90:
    print("Grade: A")
    print("Excellent")

elif marks >= 75:
    print("Grade: B")
    print("Very Good")

elif marks >= 60:
    print("Grade: C")
    print("Good")

elif marks >= 40:
    print("Grade: D")
    print("Pass")

else:
    print("Grade: F")
    print("Fail")