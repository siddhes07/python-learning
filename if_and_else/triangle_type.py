side1 = int(input("enter the first side of triangle: "))
side2 = int(input("enter the second side of triangle: "))
side3 = int(input("enter the third side of triangle: "))

if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")   