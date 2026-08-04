num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

largest = max(num1, num2)

for i in range(largest, num1 * num2 + 1):
    if i % num1 == 0 and i % num2 == 0:
        print("LCM =", i)
        break