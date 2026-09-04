nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))

seen = {}

for i, num in enumerate(nums):
    complement = target - num

    if complement in seen:
        print([seen[complement], i])
        break

    seen[num] = i