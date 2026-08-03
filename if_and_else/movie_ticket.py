'''  Movie Ticket Price

Rules:

Age	Price
Below 5	Free
5–18	₹100
19–60	₹200
Above 60	₹120 '''

age = int(input("Enter your age: "))

if age < 5:
    print("Your ticket is Free.")
elif 5 <= age <= 18:
    print("Your ticket price is ₹100.")
elif 19 <= age <= 60:
    print("Your ticket price is ₹200.")     