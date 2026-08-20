a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

if a >= b and a >= c and a >= d:
    largest = a
elif b >= a and b >= c and b >= d:
    largest = b
elif c >= a and c >= b and c >= d:
    largest = c
else:
    largest = d

print("Largest:", largest)