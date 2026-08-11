numbers = (10, 20, 30, 20, 40, 20, 50, 10)

search = int(input("Enter number to count: "))

count = 0

for num in numbers:
    if num == search:
        count += 1

print("Tuple:", numbers)
print(search, "appears", count, "times")