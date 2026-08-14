numbers = [1, 2, 3, 5, 6]

n = len(numbers) + 1

expected_sum = n * (n + 1) // 2

actual_sum = 0

for num in numbers:
    actual_sum += num

missing = expected_sum - actual_sum

print("Missing number:", missing)