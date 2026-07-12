numbers = (10, 15, 20, 25, 30, 35, 40)

even_sum = 0

for i in numbers:
    if i % 2 == 0:
        even_sum += i

print("Tuple:", numbers)
print("Sum of Even Numbers:", even_sum)