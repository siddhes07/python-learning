# Tuple program

numbers = tuple(map(int, input("Enter numbers separated by space: ").split()))

print("Tuple:", numbers)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Length:", len(numbers))
