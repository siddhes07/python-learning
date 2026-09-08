numbers = list(map(int, input("Enter numbers: ").split()))

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)

print("Even sum:", sum(even))
print("Odd sum:", sum(odd))

if len(even) > 0:
    print("Largest even:", max(even))
else:
    print("No even number")

if len(odd) > 0:
    print("Largest odd:", max(odd))
else:
    print("No odd number")
