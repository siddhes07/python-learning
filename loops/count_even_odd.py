num = int(input("Enter a number: "))

even = 0
odd = 0

for digit in str(num):
    if int(digit) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even digits =", even)
print("Odd digits =", odd)